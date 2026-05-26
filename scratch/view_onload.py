with open('c:/mh-chatbot/mh-chatbot/templates/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
onload_pos = html.find('window.onload')
if onload_pos == -1:
    onload_pos = html.find('addEventListener("DOMContentLoaded"')

if onload_pos != -1:
    print("=== DOMContentLoaded JS ===")
    print(html[onload_pos:onload_pos+2000])
else:
    # search for initialization functions
    print("No onload found, searching for DOMContentLoaded...")
