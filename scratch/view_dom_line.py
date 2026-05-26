with open('c:/mh-chatbot/mh-chatbot/templates/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'document.addEventListener("DOMContentLoaded"' in line:
        print(f"Line {i+1}: {line.strip()}")
