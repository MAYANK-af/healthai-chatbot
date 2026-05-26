with open('c:/mh-chatbot/mh-chatbot/chatbot/dialogue.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '# Skin Rash' in line:
        print(f"Skin Rash check starts at line {i+1}")
    if '# Muscle Pain' in line:
        print(f"Muscle Pain check starts at line {i+1}")
