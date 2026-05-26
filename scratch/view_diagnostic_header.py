import re

with open('c:/mh-chatbot/mh-chatbot/templates/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('Live Alert Diagnostic Logs')
if pos != -1:
    snippet = html[pos-500:pos+1500]
    ascii_snippet = re.sub(r'[^\x00-\x7F]+', '', snippet)
    print("=== DIAGNOSTIC LOGS SECTION ===")
    print(ascii_snippet)
else:
    print("Not found")
