import urllib.request
import json
import os
import sys

# Set stdout to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

from dotenv import load_dotenv

load_dotenv()

bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
if not bot_token:
    print("Error: TELEGRAM_BOT_TOKEN not found in environment or .env file.")
    sys.exit(1)

chat_id = os.environ.get("TELEGRAM_CHAT_ID", "5047061875")
medication = "aspirin"
dosage = "1 tab"
time = "08:52 (Schedule Activation Test)"

telegram_api_url = "https://api.telegram.org"
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
    'User-Agent': 'Mozilla/5.0'
}

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    url, 
    data=data, 
    headers=headers
)

try:
    with urllib.request.urlopen(req, timeout=15) as response:
        res_data = json.loads(response.read().decode('utf-8'))
        print("Success response:")
        print(json.dumps(res_data, indent=2))
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code} {e.reason}")
    print("Response body:")
    print(e.read().decode('utf-8'))
except Exception as e:
    print(f"General Exception: {str(e)}")
