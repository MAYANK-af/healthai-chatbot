with open('c:/mh-chatbot/mh-chatbot/templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all occurrences of sessionStorage with localStorage
updated_content = content.replace('sessionStorage', 'localStorage')

with open('c:/mh-chatbot/mh-chatbot/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("🎉 Successfully migrated all sessionStorage references to localStorage in templates/index.html!")
