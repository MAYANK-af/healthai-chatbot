with open('c:/mh-chatbot/mh-chatbot/templates/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# find login modal html by searching for "auth-email"
import re
auth_email_pos = html.find('auth-email')
if auth_email_pos != -1:
    start = max(0, auth_email_pos - 1000)
    end = min(len(html), auth_email_pos + 1500)
    print("=== LOGIN MODAL HTML ===")
    print(html[start:end])

# find performLogin and standard login functions
login_pos = html.find('function performLogin')
if login_pos != -1:
    print("\n=== LOGIN JS FUNCTIONS ===")
    print(html[login_pos:login_pos+2000])
