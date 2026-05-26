import re

with open('c:/mh-chatbot/mh-chatbot/chatbot/dialogue.py', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('def match_symptom_knowledgebase')
print("=== FUNCTION START ===")
snippet = html[pos:pos+1000]
print(re.sub(r'[^\x00-\x7F]+', '', snippet))

next_def_pos = html.find('def ', pos + 1)
print("\n=== NEXT FUNCTION START ===")
snippet2 = html[next_def_pos:next_def_pos+1000]
print(re.sub(r'[^\x00-\x7F]+', '', snippet2))
