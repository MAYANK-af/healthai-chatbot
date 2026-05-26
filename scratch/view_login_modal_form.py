with open('c:/mh-chatbot/mh-chatbot/templates/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

modal_pos = html.find('id="auth-form"')
if modal_pos != -1:
    print("=== AUTH FORM HTML ===")
    print(html[modal_pos:modal_pos+2000])
