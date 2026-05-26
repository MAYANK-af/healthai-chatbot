with open('c:/mh-chatbot/mh-chatbot/templates/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# find event listeners for login/auth
auth_listener_pos = html.find('document.getElementById("auth-form")')
if auth_listener_pos == -1:
    auth_listener_pos = html.find('auth-submit')

if auth_listener_pos != -1:
    print("=== LOGIN EVENT LISTENERS ===")
    print(html[auth_listener_pos-200:auth_listener_pos+2000])
else:
    # search for login form submissions
    pos = html.find('login')
    while pos != -1:
        snippet = html[pos:pos+300]
        if 'addEventListener' in snippet or 'submit' in snippet:
            print(f"Match found at index {pos}:")
            print(snippet)
            print("-" * 40)
        pos = html.find('login', pos + 1)
