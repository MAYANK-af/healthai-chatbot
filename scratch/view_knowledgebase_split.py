import re

with open('c:/mh-chatbot/mh-chatbot/chatbot/dialogue.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'def get_intent_candidates' in line:
        print(f"get_intent_candidates starts at line {i+1}")
        print("=== LINES BEFORE ===")
        for j in range(max(0, i-25), i):
            clean_line = re.sub(r'[^\x00-\x7F]+', '', lines[j])
            print(f"{j+1}: {clean_line.strip()}")
        break
