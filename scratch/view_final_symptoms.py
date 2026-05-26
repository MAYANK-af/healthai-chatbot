import re

with open('c:/mh-chatbot/mh-chatbot/chatbot/dialogue.py', 'r', encoding='utf-8') as f:
    html = f.read()

# find where get_intent_candidates starts to locate the end of dialogue symptoms
end_pos = html.find('def get_intent_candidates')
snippet = html[end_pos-4000:end_pos]
ascii_snippet = re.sub(r'[^\x00-\x7F]+', '', snippet)
print("=== FINAL SYMPTOMS SCRIPT ===")
print(ascii_snippet)
