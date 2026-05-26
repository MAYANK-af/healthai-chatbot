import re

with open('c:/mh-chatbot/mh-chatbot/templates/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Indian phone numbers' in line or 'Twilio' in line:
        # Strip all non-ascii characters for clean printing
        ascii_line = re.sub(r'[^\x00-\x7F]+', '', line)
        print(f"{i+1}: {ascii_line.strip()[:120]}")
