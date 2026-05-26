with open('c:/mh-chatbot/mh-chatbot/chatbot/dialogue.py', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = [m.start() for m in re.finditer('Symptom:', html)]
for m in matches:
    print(html[m:m+100])
    print("-" * 40)
