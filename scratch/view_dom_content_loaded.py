with open('c:/mh-chatbot/mh-chatbot/templates/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = [m.start() for m in re.finditer('DOMContentLoaded', html)]
for m in matches:
    print(html[m:m+800])
    print("-" * 40)
