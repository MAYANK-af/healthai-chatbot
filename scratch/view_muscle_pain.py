import re

with open('c:/mh-chatbot/mh-chatbot/chatbot/dialogue.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Symptom: Muscle Pain' in line or 'Joint Pain' in line:
        print(f"Muscle pain header found at line {i+1}")
        for j in range(max(0, i-5), i+2):
            clean_line = re.sub(r'[^\x00-\x7F]+', '', lines[j])
            print(f"{j+1}: {clean_line.strip()}")
        break
