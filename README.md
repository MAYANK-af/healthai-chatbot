# 🏥 HealthAI Clinical Companion (v4.6)

HealthAI is an intelligent, containerized full-stack virtual health assistant designed to bridge the gap between conversational AI, home diagnostic screening, daily vitals tracking, and medication safety. Built with a beautiful glassmorphic UI, it operates 100% locally and cost-free, offering clinical-grade safety guards and secure data exports.

🚀 **Live Interactive Demo:** [Visit your Hugging Face Space](https://huggingface.co/spaces/itachii9090/healthai-chatbot) *(Update with your direct live URL)*

---

## 🌟 Premium Core Features

### 1. Empathic Clinical Dialogue Engine
* **Sentiment-Driven Responses:** Evaluates emotional currents and distress levels to pick highly empathic, clinically tailored response patterns.
* **Proactive Follow-Ups:** Remembers recent symptoms from the checker database and proactively checks on the patient's recovery upon next login or greeting.
* **Crisis Safety Routing:** Detects high-risk crisis triggers instantly and overlays a dedicated help panel with official national and international helplines.

### 2. Ultimate 35-Symptom Screening Matrix
* **Natural Language Matching:** Utilizes flexible, word-order-independent regular expressions to match natural language complaints for **35 major physical symptoms** with 100% precision.
* **Four Standardized Clinical Sections:** Generates highly structured, compliant clinical guides for every matched symptom, containing:
  1. *Clinical Assessment:* Medical breakdown of potential root causes.
  2. *At-Home Cures:* Immediate, drug-free physiological relief guidelines.
  3. *OTC Medications:* Targeted, chemical-compound-specific OTC suggestions with strict safety advisories.
  4. *🚨 Emergency Red Flags:* Vital warnings that require immediate professional or emergency care.
* **Robust Verification:** Backed by an automated test suite (`scratch/test_all_symptoms.py`) yielding a **100% validation success rate**.

### 3. Integrated Bio-Risk / Wellness Index Dial
* **Holistic Score Calculation:** A real-time physiological dial that dynamically aggregates vital indicators into a **0% to 100% Wellness Index**:
  * *Resting Heart Rate (25%):* Deducts points for tachycardic or bradycardic deviations.
  * *Sleep Quality (25%):* Scales sleep hours, flagging borderline or severe sleep deficits.
  * *Hydration (25%):* Tracks progress against a daily 2000 ml goal.
  * *Emotional Balance (25%):* Integrates score parameters directly from your latest Mindfulness Journal entry.
* **Symptom Tracker Deductions:** Automatically deducts 10 points per active symptom (up to a 30-point max) if a physical symptom assessment was completed within the last 15 minutes.
* **Dynamic Glassmorphic Dial:** Center-aligned percentage score inside an SVG progress circle that dynamically updates its stroke colors (Green for excellent, Amber for mild concerns, Red for high-risk indices) and compiles clinical concern alerts.

### 4. Mindfulness Journal & 7-Entry SVG Mood Trend Chart
* **Client-Side Sentiment Classifier:** Scans private reflections for stress, anxiety, or fatigue indicators, categorizing entries into *Positive, Neutral, Anxious,* or *Negative* states.
* **7-Entry Mood Trend SVG Chart:** A responsive, interactive, and color-coded SVG sparkline bar chart. Includes horizontal grid-line thresholds, white-capped dots, and hover-triggered tooltips showing the date, score, and full entry text.
* **Personalized Voice Coach Pacing:** Automatically updates the guided breathing coach's box-breathing pace selector based on emotional currents:
  * *Positive / Neutral* $\rightarrow$ **Standard 4s** (Balanced nervous care).
  * *Anxious / Stressed* $\rightarrow$ **Deep 5s** (Vagal stimulation to lower heart rate and cortisol).
  * *Negative / Sad / Tired* $\rightarrow$ **Quick 3s** (Resets respiratory drive and stimulates energy levels).

### 5. Stateful Pill Organizer & Allergy Alert Guard
* **Stateful Regimen Scheduler:** Build complete daily medication routines with customized dosages, frequencies, and exact administration times.
* **100% Free HTTPS Telegram Alerts:** Integrates an active background scheduler (`APScheduler`) that sends real-time medication alerts directly to your phone via Telegram Bot APIs (SSL-timeout and Cloudflare proxy compliant).
* **Clinical Contraindication Scanner:** Instantly flags drug-drug interactions (e.g., SSRIs + NSAIDs upper GI hemorrhage warnings or vaso-constricting decongestants + Hypertension warnings).
* **Stateful Allergy Guard:** Cross-references scheduled medications against diagnosed allergies on your **Health Card**. Displays red warnings for major classes:
  * *Penicillin Class:* Rashes/anaphylaxis alerts for Amoxicillin, Augmentin, etc.
  * *Sulfa Class:* Cutaneous adverse reactions alerts for Bactrim, Septra, etc.
  * *Aspirin / NSAID Class:* Bronchospasm hazards for Ibuprofen, Naproxen, Advil, etc.

### 6. On-Demand Secure Intake Exports (PDF & Telegram)
* **One-Click Clinician PDF:** Compiles patient demographics, chronic history, emergency contacts, synced vitals, and scheduled medications into a clean, grid-based clinical summary and triggers browser print-to-PDF options.
* **Secure Telegram File Dispatch:** Compiles active card records, manual logs, and scheduled regimens into a beautifully formatted plain-text document (`HealthAI_Medical_Card.txt`) and uploads it directly to your Telegram chat with one click.

### 7. Professional SaaS State Management
* **LocalStorage Permanent Database:** Login, signup, profiles, and historical logs are permanently persisted under specific user namespaces. Logging in or out automatically reloads and synchronizes all cards, resolving stale data screens.
* **Developer Console Controls:** An elegant Diagnostics Visibility button allows end-users to collapse the live technical developer terminal and persist their collapse preferences permanently across page refreshes.

---

## 🛠️ Technological Stack

* **Backend Engine:** Python 3.10, Flask (Session, JSON APIs, Routing)
* **Scheduling & Reminders:** APScheduler (Advanced Python Scheduler)
* **Natural Language NLP:** NLTK (Natural Language Toolkit)
* **Frontend Interface:** HTML5 (Semantic Structure), CSS3 (Vanilla Glassmorphic Stylesheets & Tailwind utility components), JavaScript (Event Loop, DOM Manipulation, SVG Charts, LocalStorage, Web Audio Speech Synthesis)
* **Containerization & Hosting:** Docker (Multi-stage build), Gunicorn, Hugging Face Hub APIs

---

## 📁 Directory Structure
```
mh-chatbot/
├── app.py                  # Flask Application Core Server & Telegram Dispatch APIs
├── requirements.txt        # Backend dependencies
├── Dockerfile              # Containerization configuration for HF Spaces compliance
├── upload_to_hf.py         # Automated, lightweight folder-uploader script (ignores .venv)
├── templates/
│   └── index.html          # Unified Dashboard UI (HTML5, Tailwind, CSS, JS Engine)
├── static/
│   └── style.css           # Glassmorphic color systems, visual metrics, and keyframes
├── chatbot/
│   ├── model.py            # NLP Sentiment & Crisis Intent classification engine
│   ├── dialogue.py         # 35-Symptom regex matching & clinical guide database
│   └── resources.py        # National & International Emergency clinical helplines
└── scratch/
    ├── test_all_symptoms.py# Comprehensive 35-symptom automated validation script
    └── check_syntax.js     # VM-based script compiler validator
```

---

## ⚙️ Running Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mayank-22/Mayank-AI.git
   cd mh-chatbot
   ```

2. **Initialize a Virtual Environment & Install Dependencies:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate       # On Windows PowerShell
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root folder:
   ```env
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   GOOGLE_CLIENT_ID=your_google_sign_in_id_here
   ```

4. **Launch the Server:**
   ```bash
   python app.py
   ```
   Open `http://127.0.0.1:5000` in your web browser.

---

## 📤 Automated Deployment to Hugging Face
To push updates directly to your live website in seconds without manual dragging-and-dropping:
```bash
.venv\Scripts\python upload_to_hf.py
```
Enter your Hugging Face username, Space repository name, and Write Token when prompted.

---

## 👤 Author
**Mayank Yadav**
*B.Tech Computer Science — Manipal University Jaipur*  
✉️ my1220301@gmail.com  
🔗 [GitHub Profile](https://github.com/Mayank-22)
