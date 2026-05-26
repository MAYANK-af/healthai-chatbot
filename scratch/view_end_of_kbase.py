import re

with open('c:/mh-chatbot/mh-chatbot/chatbot/dialogue.py', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('def get_intent_candidates')
if pos != -1:
    snippet = html[pos-1500:pos]
    ascii_snippet = re.sub(r'[^\x00-\x7F]+', '', snippet)
    print("=== END OF KBASE SNIPPET ===")
    print(ascii_snippet)
else:
    print("get_intent_candidates not found")
