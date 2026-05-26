with open('c:/mh-chatbot/mh-chatbot/templates/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = [m.start() for m in re.finditer('health-card', html)]
for m in matches[:10]:
    print(html[m:m+150])
    print("-" * 40)
