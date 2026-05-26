with open('c:/mh-chatbot/mh-chatbot/templates/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('tabLogin.addEventListener')
if pos != -1:
    print("=== TAB SWITCH JS ===")
    print(html[pos:pos+1500])
