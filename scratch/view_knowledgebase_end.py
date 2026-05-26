with open('c:/mh-chatbot/mh-chatbot/chatbot/dialogue.py', 'r', encoding='utf-8') as f:
    html = f.read()

pos = html.find('def match_symptom_knowledgebase')
end_pos = html.find('def get_response')

print(f"Symptom knowledgebase function characters length: {end_pos - pos}")
print("=== END OF SYMPTOM KNOWLEDGEBASE ===")
print(html[end_pos-1500:end_pos])
