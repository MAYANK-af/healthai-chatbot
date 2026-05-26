with open('c:/mh-chatbot/mh-chatbot/chatbot/dialogue.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '# Stiff Neck' in line:
        print(f"Stiff Neck at line {i+1}")
    if '# Dry Skin' in line:
        print(f"Dry Skin at line {i+1}")
