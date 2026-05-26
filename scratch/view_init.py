with open('c:/mh-chatbot/mh-chatbot/templates/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('syncScheduledAlertsWithBackend')
while pos != -1:
    print(html[pos-100:pos+500])
    print("-" * 40)
    pos = html.find('syncScheduledAlertsWithBackend', pos + 1)
