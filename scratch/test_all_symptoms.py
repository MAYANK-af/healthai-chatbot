import sys
sys.path.append('c:/mh-chatbot/mh-chatbot')
from chatbot.dialogue import get_response

# Set stdout to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

symptom_tests = [
    ("MY EYES ARE BURNING", "Eye Burning"),
    ("i feel chest pain and my heart is racing", "Chest Pain"),
    ("i can't breathe and am wheezing severely", "Shortness of Breath"),
    ("my throat is extremely sore and it hurts to swallow", "Sore Throat"),
    ("my ear is clogged and aching", "Earache"),
    ("i feel dizzy and the room is spinning", "Dizziness"),
    ("it burns when i pee", "Urinary Burning"),
    ("i have a red itchy skin rash", "Skin Rash"),
    ("my tooth is throbbing and gums are bleeding", "Toothache"),
    ("i haven't pooped in three days and feel constipated", "Constipation"),
    ("i have watery diarrhea and stomach flu", "Diarrhea"),
    ("i have a hacking dry cough", "Cough"),
    ("my body temperature is 102 degrees and I have high fever", "Fever"),
    ("my lower back pain is stiff and sore", "Muscle Pain"),
    ("MY JOINTS HURTS", "Muscle Pain"),
    ("i have a terrible throbbing migraine headache", "Headache"),
    ("i feel nauseous and threw up", "Nausea"),
    ("i am feeling extremely weak and fatigued", "Fatigue"),
    ("i have a sour acid taste in my throat and bad heartburn", "Acid Reflux"),
    ("my nose is stuffy and severely congested", "Nasal Congestion"),
    ("i am sneezing a lot due to pollen allergies", "Allergic Reaction"),
    # New Symptoms (v3.9 - 21 to 30)
    ("i am struggling with chronic insomnia and sleeplessness", "Insomnia"),
    ("i have a painful canker sore inside my mouth", "Canker Sores"),
    ("my heart is skipping beats and fluttering", "Heart Palpitations"),
    ("i have neck stiffness and stiff muscle pain", "Stiff Neck"),
    ("i feel bloated with trapped gas pain", "Stomach Gas"),
    ("burning in my stomach and acidic cramps", "Acidic Stomach"),
    ("i have flaky dry skin and chapped lips", "Dry Skin"),
    ("my eye is red and bloodshot with conjunctivitis", "Red Eyes"),
    ("loss of sensation and tingling pins and needles in foot", "Numbness"),
    ("sunburn on my shoulders and minor burns", "Minor Burn"),
    # New Symptoms (v4.0 - 31 to 35)
    ("i have a painful cold sore blister on my lip", "Cold Sores"),
    ("my hair is thinning and falling out in clumps", "Hair Loss"),
    ("i woke up with a painful leg cramp in my calf", "Leg Cramps"),
    ("my mouth feels completely dry and sticky with no saliva", "Dry Mouth"),
    ("my toenails look yellow, thick, and brittle due to nail fungus", "Nail Fungus")
]

print("=" * 70)
print("TESTING 35-SYMPTOM CLINICAL KNOWLEDGEBASE MATCHES (v4.0)")
print("=" * 70)

all_passed = True
for query, expected_name in symptom_tests:
    response = get_response(query, "neutral", "medium", [])
    if response and expected_name.lower() in response.lower():
        print(f"✅ PASSED: '{query}' -> matched expected guide '{expected_name}'")
    else:
        print(f"❌ FAILED: '{query}' -> expected '{expected_name}', got response starting with:")
        print(f"   {str(response)[:120] if response else 'None'}")
        all_passed = False

print("=" * 70)
if all_passed:
    print("🏆 SUCCESS: All 35 clinical symptoms matched their guides successfully!")
else:
    print("⚠️ WARNING: Some symptom matches failed. Please inspect.")
print("=" * 70)
