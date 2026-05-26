import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
if not bot_token:
    print("Error: TELEGRAM_BOT_TOKEN not found in environment or .env file.")
    sys.exit(1)

url = f"https://api.telegram-proxy.org/bot{bot_token}/getMe"

try:
    with urllib.request.urlopen(url, timeout=15) as response:
        res_data = json.loads(response.read().decode('utf-8'))
        print("Telegram-Proxy.org Success:")
        print(json.dumps(res_data, indent=2))
except Exception as e:
    print(f"Exception for telegram-proxy.org: {str(e)}")
