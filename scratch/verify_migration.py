with open('c:/mh-chatbot/mh-chatbot/templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

count = content.count('sessionStorage')
print(f"Remaining sessionStorage count: {count}")
