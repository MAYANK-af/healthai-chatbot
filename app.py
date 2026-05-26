import os
import uuid
import urllib.request
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify, session

# Dialog systems
from chatbot.model import classify_sentiment
from chatbot.dialogue import get_response
from chatbot.resources import get_resources

# Notification integrations
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv

# Load environmental variables
load_dotenv()

app = Flask(__name__)
app.secret_key = "mhchatbot-secret-key"

# Live alert diagnostics queue
notification_logs = []

def add_notification_log(status, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notification_logs.append({"timestamp": timestamp, "status": status, "message": message})
    if len(notification_logs) > 20:
        notification_logs.pop(0)

# Initialize background scheduler to manage exact notification time triggers recurring daily
scheduler = BackgroundScheduler()
scheduler.start()

# ==================== REMINDER DISPATCH CORE ENGINE ====================

def send_telegram_reminder(chat_id, medication, dosage, time):
    """Sends a real Telegram message using standard urllib over HTTPS. Supports proxying via TELEGRAM_API_URL."""
    try:
        bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
        if not bot_token:
            sim_msg = f"Simulated Telegram to {chat_id}: Take {medication} ({dosage}) at {time}"
            print(f"⚠️ Telegram Token not configured. {sim_msg}")
            add_notification_log("warning", f"Telegram Bot Token missing (Simulation Mode). {sim_msg}")
            return False

        telegram_api_url = os.environ.get("TELEGRAM_API_URL", "https://api.telegram.org").rstrip('/')
        url = f"{telegram_api_url}/bot{bot_token}/sendMessage"
        
        body_text = (
            f"🔔 *HealthAI Medication Reminder* 🔔\n\n"
            f"Hello Mayank! It is time to take your medication:\n"
            f"💊 *{medication}* ({dosage})\n"
            f"⏰ Scheduled for: {time}\n\n"
            f"Please reply when taken to log your adherence."
        )
        
        payload = {
            "chat_id": chat_id,
            "text": body_text,
            "parse_mode": "Markdown"
        }
        
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(
            url, 
            data=data, 
            headers=headers
        )
        
        with urllib.request.urlopen(req, timeout=15) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            if res_data.get("ok"):
                success_msg = f"Telegram sent successfully to Chat ID {chat_id}!"
                print(f"✅ {success_msg}")
                add_notification_log("success", success_msg)
                return True
            else:
                err_msg = f"Telegram API error: {res_data.get('description')}"
                print(f"❌ {err_msg}")
                add_notification_log("error", err_msg)
                return False
    except Exception as e:
        err_msg = f"Failed to dispatch Telegram to {chat_id}: {str(e)}"
        print(f"❌ {err_msg}")
        add_notification_log("error", err_msg)
        return False

# ==================== ENDPOINTS & ROUTING ====================

@app.route("/")
def index():
    session["history"] = []
    google_client_id = os.environ.get("GOOGLE_CLIENT_ID", "")
    return render_template("index.html", google_client_id=google_client_id)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()
    client_history = request.json.get("history")
    symptoms = request.json.get("symptoms", [])
    
    if not user_message:
        return jsonify({"response": "I'm here. Please feel free to share what's on your mind."})

    if client_history is not None:
        history = list(client_history)
    else:
        if "history" not in session:
            session["history"] = []
        history = session["history"]

    sentiment, severity = classify_sentiment(user_message)
    response = get_response(user_message, sentiment, severity, history, symptoms)

    history.append({"user": user_message, "bot": response, "sentiment": sentiment})
    history = history[-10:]
    session["history"] = history

    result = {
        "response": response,
        "sentiment": sentiment,
        "history": history
    }
    if severity == "crisis":
        result["resources"] = get_resources()
    return jsonify(result)

@app.route("/schedule-med-alert", methods=["POST"])
def schedule_med_alert():
    """Register medication alert inside flask background scheduler"""
    data = request.json or {}
    med_name = data.get("name")
    dosage = data.get("dosage")
    exact_time = data.get("exactTime")  # e.g., "08:30" (24h format)
    alert_pref = data.get("alertPref")  # "telegram" or "none"
    contact = data.get("alertContact")
    
    if alert_pref == "none" or not contact or not exact_time:
        return jsonify({"status": "no_alert_configured"})
    
    try:
        hour, minute = map(int, exact_time.split(":"))
    except ValueError:
        return jsonify({"error": "Invalid time format"}), 400
        
    job_id = f"job_{med_name.lower().replace(' ', '_')}_{contact.replace(' ', '_')}"
    
    if alert_pref == "telegram":
        scheduler.add_job(
            send_telegram_reminder,
            trigger="cron",
            hour=hour,
            minute=minute,
            id=job_id,
            args=[contact, med_name, dosage, exact_time],
            replace_existing=True
        )
        # Dispatch immediate test verification check
        send_telegram_reminder(contact, med_name, dosage, f"{exact_time} (Schedule Activation Test)")
        
    return jsonify({
        "status": "scheduled",
        "job_id": job_id,
        "trigger_time": f"{hour:02d}:{minute:02d} daily"
    })

@app.route("/delete-med-alert", methods=["POST"])
def delete_med_alert():
    """Delete a configured alert job when a medication is deleted from schedule"""
    data = request.json or {}
    med_name = data.get("name")
    contact = data.get("alertContact")
    
    if not med_name or not contact:
        return jsonify({"status": "no_job_found"})
        
    job_id = f"job_{med_name.lower().replace(' ', '_')}_{contact.replace(' ', '_')}"
    
    try:
        if scheduler.get_job(job_id):
            scheduler.remove_job(job_id)
            print(f"🗑️ Successfully removed scheduled job: {job_id}")
            return jsonify({"status": "deleted", "job_id": job_id})
    except Exception as e:
        print(f"⚠️ Failed to remove scheduled job: {e}")
        
    return jsonify({"status": "not_found"})

# ==================== SECURE TELEGRAM DOCUMENT DISPATCH ====================

def send_telegram_document(chat_id, file_content, file_name):
    """Sends a plain-text medical summary document to Telegram over HTTPS."""
    try:
        bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
        if not bot_token:
            sim_msg = f"Simulated Telegram File: {file_name} sent to {chat_id}"
            print(f"⚠️ Telegram Token not configured. {sim_msg}")
            add_notification_log("warning", f"Telegram Token missing (Simulation Mode). {sim_msg}")
            return True, "Simulated report sent successfully (Telegram bot token missing)."

        telegram_api_url = os.environ.get("TELEGRAM_API_URL", "https://api.telegram.org").rstrip('/')
        url = f"{telegram_api_url}/bot{bot_token}/sendDocument"
        
        boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
        parts = []
        
        # chat_id field
        parts.append(f"--{boundary}")
        parts.append('Content-Disposition: form-data; name="chat_id"')
        parts.append("")
        parts.append(str(chat_id))
        
        # document field
        parts.append(f"--{boundary}")
        parts.append(f'Content-Disposition: form-data; name="document"; filename="{file_name}"')
        parts.append("Content-Type: text/plain")
        parts.append("")
        parts.append(file_content)
        
        parts.append(f"--{boundary}--")
        parts.append("")
        
        body = "\r\n".join(parts).encode('utf-8')
        
        headers = {
            'Content-Type': f'multipart/form-data; boundary={boundary}',
            'Content-Length': str(len(body)),
            'User-Agent': 'Mozilla/5.0'
        }
        
        req = urllib.request.Request(url, data=body, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            if res_data.get("ok"):
                return True, "Report document sent successfully!"
            else:
                return False, f"Telegram API error: {res_data.get('description')}"
    except Exception as e:
        return False, f"Failed to dispatch Telegram document to {chat_id}: {str(e)}"

@app.route("/send-tele-report", methods=["POST"])
def send_tele_report():
    """Compiles and dispatches patient clinical card and vitals as a text file over Telegram."""
    data = request.json or {}
    chat_id = data.get("chat_id")
    profile = data.get("profile", {})
    vitals = data.get("vitals", {})
    pills = data.get("pills", [])
    
    if not chat_id:
        return jsonify({"error": "Telegram Chat ID is required"}), 400
        
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report_lines = [
        "============================================================",
        "                 HEALTHAI MEDICAL CARD REPORT               ",
        "============================================================",
        f"Generated on: {timestamp}",
        "",
        "------------------------------------------------------------",
        "1. PATIENT DEMOGRAPHICS & PROFILE",
        "------------------------------------------------------------",
        f"Patient Name:       {profile.get('name', 'N/A')}",
        f"Email Address:      {profile.get('email', 'N/A')}",
        f"Blood Type:         {profile.get('bloodType', 'N/A')}",
        f"Emergency Contact:  {profile.get('emergencyContact', 'N/A')}",
        "",
        "------------------------------------------------------------",
        "2. PATIENT CLINICAL HISTORY",
        "------------------------------------------------------------",
        f"Chronic Conditions: {profile.get('conditions', 'None registered')}",
        f"Drug Allergies:     {profile.get('allergies', 'None registered')}",
        "",
        "------------------------------------------------------------",
        "3. ACTIVE RESTING VITALS (LOGGED STATE)",
        "------------------------------------------------------------",
        f"Resting Heart Rate: {vitals.get('hr', 'N/A')} bpm",
        f"Sleep Duration:     {vitals.get('sleep', 'N/A')} hours",
        f"Water Intake:       {vitals.get('hydration', 'N/A')} ml",
        f"Active Calories:    {vitals.get('calories', 'N/A')} kcal",
        "",
        "------------------------------------------------------------",
        "4. ACTIVE MEDICATION SCHEDULE & DOSAGES",
        "------------------------------------------------------------"
    ]
    
    if not pills:
        report_lines.append("No active medications are currently scheduled in the Pill Organizer.")
    else:
        for idx, pill in enumerate(pills):
            time_str = pill.get('exactTime', 'N/A')
            report_lines.append(f"{idx+1}. Drug:     {pill.get('name', 'N/A')}")
            report_lines.append(f"   Dosage:   {pill.get('dosage', 'N/A')}")
            report_lines.append(f"   Schedule: {pill.get('freq', 'N/A')} at {time_str}")
            report_lines.append("")
            
    report_lines.append("------------------------------------------------------------")
    report_lines.append("                 END OF CLINICAL INTAKE SUMMARY            ")
    report_lines.append("============================================================")
    
    report_text = "\n".join(report_lines)
    file_name = f"HealthAI_Medical_Card_{profile.get('name', 'Patient').replace(' ', '_')}.txt"
    
    success, msg = send_telegram_document(chat_id, report_text, file_name)
    
    if success:
        add_notification_log("success", f"Medical card file dispatched to Chat ID {chat_id}!")
        return jsonify({"status": "success", "message": msg})
    else:
        add_notification_log("error", f"Failed to send medical card file: {msg}")
        return jsonify({"error": msg}), 500

@app.route("/api/notification-logs", methods=["GET"])
def get_notification_logs():
    """Retrieve visual notification delivery diagnostic logs list"""
    return jsonify(notification_logs)

if __name__ == "__main__":
    app.run(debug=True)
