with open('c:/mh-chatbot/mh-chatbot/templates/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

modal_pos = html.find('id="login-modal"')
if modal_pos != -1:
    print("=== LOGIN MODAL HTML ===")
    print(html[modal_pos:modal_pos+3000])
else:
    print("Login modal not found, searching for id containing 'login'...")
    # search for login classes or IDs
    pos = html.find('login')
    while pos != -1:
        snippet = html[pos-50:pos+250]
        if 'modal' in snippet:
            print(f"Index {pos}: {snippet}")
        pos = html.find('login', pos + 1)
