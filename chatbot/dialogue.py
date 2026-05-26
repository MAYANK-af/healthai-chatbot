import random
import re

RESPONSES = {
    "crisis": [
        "I am so glad you reached out, and I want you to know with absolute certainty that **you are not alone, and you do not have to carry this immense weight by yourself.** What you are feeling right now is incredibly heavy, and you deserve a safe space and real, immediate support. \n\n**Please connect with a trained professional right away.** They are ready to listen with profound compassion, 24/7, completely free and confidential:\n* **National Suicide & Crisis Lifeline:** Call or text **988** (Available 24/7)\n* **The Crisis Text Line:** Text **HOME to 741741**\n* **International Helplines:** If you are outside the US, please visit [Befrienders Worldwide](https://www.befrienders.org/) to find local support.\n\nI am keeping you in my thoughts. Please take that brave step and reach out to them now. You matter so much.",
        "Thank you for being here and trusting me with what you are experiencing. Please hear me: **your life is extremely valuable, and there is support waiting for you right now.** \n\nBecause your safety is the absolute priority, please contact a professional crisis service immediately. They are dedicated, trained to listen without judgment, and want to support you through this exact moment:\n* **Call or Text 988** to reach the Suicide & Crisis Lifeline.\n* **Text HOME to 741741** to connect with a crisis counselor.\n\nThese resources are completely free, confidential, and available 24/7. Please let a compassionate professional wrap support around you today."
    ],
    "distressed_high": [
        "I hear how incredibly heavy and painful things are for you right now, and I want to validate that **it is completely okay to feel overwhelmed.** You have been holding so much together, and it takes real courage to open up about it. \n\nI am right here with you. If you feel up to it, what has been the hardest part for you to cope with lately? We can take this completely at your own pace, one gentle step at a time.",
        "It sounds like you are standing in the middle of a very heavy storm, and I want you to know that **you don't have to navigate this darkness alone.** Your feelings are completely valid, and I am here to listen with deep care.\n\nLet's take a slow breath together. What is on your mind or heart that feels the most pressing right now? I am in your corner, and I am listening.",
        "I am so sorry that you are carrying such an intense amount of pain today. Please know that **your feelings are heard, they are valid, and I am here to support you.** \n\nSometimes when the pressure builds up, putting even a small piece of it into words can help release a little bit of that tension. What is one thing you would like to vent or share with me right now? There is absolutely no pressure.",
        "I can feel the depth of what you're experiencing through your words, and it makes complete sense that you feel this overwhelmed. **Please be gentle with yourself right now.** \n\nI am here to listen to anything you want to share. Are you sleeping or eating okay physically, or has this emotional stress been taking a heavy toll on your body?"
    ],
    "distressed_medium": [
        "Thank you for being honest with me about how you're feeling. **It is completely okay to not be okay,** and you never have to put on a brave face when you're talking with me. \n\nWhat you're going through sounds incredibly challenging. How long have you been carrying these heavy feelings? I'm here to listen.",
        "I can hear how much this is weighing on you, and I want to pause and send you a gentle virtual hug. **Your feelings make complete sense given what you're dealing with.** \n\nWhat is one small thing that has felt even slightly comforting or supportive to you today? Let's focus on just getting through this day, step by step.",
        "I'm really sorry that things feel so difficult and draining right now. **Please know that you are in a safe, non-judgmental space.** \n\nSometimes it helps to look at what might have triggered these feelings. Did something specific happen recently, or has this been building up slowly over time? I'm here for whatever you want to share.",
        "That sounds really tough, and I want to validate how exhausting it is to feel this way. **You are doing the best you can, and that is more than enough.** \n\nWould it feel helpful to talk through what is going on, or would you prefer some simple, comforting wellness techniques to help quiet your mind? I'm here to support you in whatever way feels best."
    ],
    "negative": [
        "It sounds like things have been incredibly rough and exhausting lately. I'm so sorry you're facing these hurdles. I'm right here to listen — what has been going on in your world?",
        "That doesn't sound easy at all, and I can hear the frustration or sadness in your words. **Your feelings are completely valid.** Would you like to unpack it together, or do you just need to vent and let it out?",
        "I'm really sorry to hear you're feeling down. What has been occupying your thoughts the most today? I'm here to listen and carry a bit of this weight with you.",
        "I deeply appreciate you being so open and honest with me about how you feel. I am here to support you. What do you think would help you feel even 1% more supported or comfortable right now?"
    ],
    "positive": [
        "That is absolutely wonderful to hear! I am smiling reading this. **You deserve these moments of joy and lightness.** What has been going well for you today?",
        "It makes me so happy to hear that things are looking up for you! Celebrate these moments — they are so important. Tell me more about what is making you feel good!",
        "That is fantastic news! **Acknowledge and celebrate these positive feelings.** What led to this beautiful wave of positive energy in your day?",
        "Love to hear that! Keep that beautiful, positive energy going. What are you looking forward to next in your week?"
    ],
    "neutral": [
        "I am so glad you reached out today. I am right here and listening closely. How are you really doing lately?",
        "Hello! I am happy you're here. What is on your mind today? Feel free to share anything, big or small.",
        "I'm glad you stopped by to chat. I'm here to support you in any way I can. What's been happening in your day?",
        "Always happy to chat with you. What is new in your world, or is there a specific topic you would like to explore today?"
    ],
    "followup_distressed": [
        "Thank you for sharing that with me. Have you been able to talk to anyone close to you — like a trusted friend, family member, or a professional — about what you're carrying? Having support in your offline life is so vital.",
        "That makes a lot of sense, and it sounds so exhausting. Have you felt this way before, or is this a relatively new storm you're navigating?",
        "You are being incredibly brave by opening up to me. Is there anything specific that triggered these feelings recently, or does it feel more like a general weight?",
        "Thank you for letting me in. How are you taking care of your physical body right now? Are you sleeping, hydrating, or eating okay? Our physical well-being is so closely tied to our emotional health.",
        "It is completely okay to take all the time you need. What is one small, simple comfort — like a warm cup of tea, a cozy blanket, or a favorite song — that usually helps you feel a bit safer or calmer?"
    ],
    "followup_general": [
        "How has that been affecting your day-to-day routine and your energy levels lately?",
        "Is there anything that has been helping you cope or get through the day, even in a very small way?",
        "What does a typical, gentle day look like for you right now? I'd love to understand your world a bit better.",
        "I hear you completely. What do you think would help you feel even slightly more supported or comfortable today?",
        "That is really interesting. Tell me more about how you feel about that."
    ]
}

INTENT_RESPONSES = {
    "greeting": [
        "Hello! I am your AI Health and Wellness Assistant. **I am here to support you, listen with deep empathy, and guide you toward comforting resources.** \n\nHow are you really feeling today? Please feel free to share whatever is on your mind.",
        "Hi there! I am so glad you reached out. I am here to listen, offer a safe, warm space for your thoughts, and help support your mental wellness. \n\nWhat is weighing on your mind or heart today?",
        "Hey! Welcome. I am your personal health and wellness companion. **Please know this is a safe, non-judgmental space.** \n\nFeel free to share how you're feeling, or ask me any questions about wellness, symptoms, or medications!"
    ],
    "capabilities": [
        "I am equipped to support you in several meaningful ways! Here is what we can do together:\n\n* **Empathetic Listening & Support:** You can chat with me about how you're feeling, stress, or anxiety anytime. I am here to validate and support you.\n* **Interactive Symptom Checker:** Scroll down to input symptoms, calculate a severity index, and get gentle educational guidelines.\n* **FDA Medication Reference:** Look up common over-the-counter and prescription medications, side effects, and warnings.\n* **Wellness Tips:** Explore daily health habits, guided box breathing, and mindfulness practices.\n* **Clinical Research:** Search real-time medical and clinical trials.\n\nHow can I best support you in this moment?",
        "As your dedicated AI companion, I am here to walk alongside you on your wellness journey. You can check out our **Resources Hub** in the tabs below to use the Symptom Checker, search our Medication Guide, or read daily Wellness Tips. \n\nOf course, if you just need a caring, empathetic listening ear to talk through how you're feeling, I am always right here."
    ],
    "anxiety": [
        "I hear how incredibly overwhelming and scary this feels right now, and I want to validate that **your feelings are real, and you are safe here.** Anxiety can flood your mind and make your body feel like it is in immediate danger, but this feeling *will* pass. \n\nLet's take a slow, gentle breath together to help soothe your nervous system. Try to follow this box-breathing step:\n* **Inhale** slowly through your nose for 4 seconds...\n* **Hold** that breath gently for 4 seconds...\n* **Exhale** completely through your mouth for 4 seconds...\n* **Rest** in that stillness for 4 seconds...\n\nCan you describe 2 or 3 solid things you can see or touch right now? Bringing your awareness back to your physical space can help ground you.",
        "Anxiety can feel so physical and frightening, causing your heart to race and your chest to feel tight. Please know **you are safe, you are here, and you are going to be okay.** \n\nLet's try a simple grounding exercise together to help quiet the alarm in your body:\n* Focus on the feeling of your feet pressing firmly against the floor.\n* Take a slow, deep breath in... and let it out with a quiet sigh.\n* Tell me about 3 comforting things or sights in your immediate surroundings.\n\nI am right here with you, and we can take all the time you need."
    ],
    "sleep": [
        "When your mind is racing, sleep can feel completely out of reach, and I know how frustrating and exhausting that is. **Please be gentle with yourself — struggling with sleep is incredibly common.**\n\nTo help transition your mind and body into a restful state, try these gentle sleep habits:\n* **Dim the lights** and step away from all digital screens at least 45 minutes before bed.\n* Keep your bedroom cool, dark, and quiet.\n* Try a warm shower or sip some non-caffeinated herbal tea (like Chamomile).\n* Focus on relaxing one muscle group at a time, starting from your toes and working up to your forehead.\n\nHave you had trouble sleeping for a long time, or is this restlessness relatively new?",
        "I hear how tiring it is when sleep simply won't come. When insomnia strikes, **the pressure to fall asleep can actually keep us awake.** \n\nLet's try a technique called **Cognitive Shuffling** to distract your brain:\n* Think of a random word, like 'CALM'.\n* For each letter (C, A, L, M), think of 5 slow words that start with that letter (e.g., Cat, Cloud, Cup...). \n* This gentle exercise triggers your brain's natural transition into a dreaming, relaxed state.\n\nWould you like to try this, or would you prefer a simple breathing wind-down routine?",
        "Struggling to fall asleep is incredibly exhausting, and it is completely natural to feel frustrated when you're staring at the clock. \n\nHere are some classic sleep hygiene steps to quiet your racing thoughts:\n* If you are still awake after 20 minutes, **get out of bed.** Go to a dim corner and read a book or journal until you feel heavy-eyed.\n* Avoid looking at the clock, as it triggers anxiety loops.\n* Try counting backwards from 300 by 3s in your head to slow down brainwave activity.\n\nLet's take a slow breath. You are doing great, and rest will find you."
    ],
    "headache": [
        "Headaches can be so disruptive, exhausting, and physically draining. I'm really sorry you're dealing with this head pain today.\n\nHere are a few gentle, drug-free steps that often help provide relief:\n* **Hydration is key:** Drink a large, cool glass of water, as dehydration is one of the most common headache triggers.\n* **Rest your eyes:** Step away from digital screens, turn down the lights, and rest in a quiet, dark room.\n* **Apply temperature:** Put a cool compress on your forehead or a warm heating pad on your neck to release muscle tension.\n* **Massage:** Gently rub your temples or the base of your skull in slow, circular motions.\n\n*Important Notice: If this is a sudden, unusually severe headache, or if it is accompanied by a stiff neck, high fever, confusion, or changes in your vision, please consult a healthcare professional immediately.*",
        "I'm so sorry your head is throbbing and hurting. Headaches can truly drain your energy and make it impossible to concentrate. \n\nHere is a simple progressive relaxation method to help relieve tension:\n* Close your eyes and raise your shoulders to your ears, holding for 5 seconds. Then let them drop completely with a long, slow exhale.\n* Gently rotate your head in small, slow circles to stretch out your neck muscles.\n* Take a 15-minute complete screen break — step away from phones, tablets, and computers.\n\nHave you had water to drink recently, or did this headache start after a long day of screen exposure?",
        "I can hear how much discomfort you're in from this headache, and I want to send you some comforting energy. \n\nTo help support your recovery:\n* Drink a tall glass of water or electrolyte fluid immediately.\n* Sit in a comfortable position and place a damp, cool cloth over your eyes to block out light and soothe nerves.\n* Take 5 slow, deep breaths, letting your abdomen rise and fall naturally.\n\nRemember to consult a professional if this headache feels completely different from past aches, or if it is accompanied by severe nausea or changes in your speech."
    ],
    "stomach": [
        "Stomach aches, nausea, or digestive distress can make you feel so uncomfortable and depleted. I'm really sorry you're feeling unwell.\n\nTo help support your stomach and digestive system right now:\n* **Stick to the BRAT diet:** Toast, rice, applesauce, or crackers are very gentle on an upset stomach.\n* **Stay hydrated:** Take small, frequent sips of warm water, clear broths, or warm ginger or peppermint tea.\n* **Apply gentle heat:** Place a hot water bottle or a heating pad on your abdomen to help soothe cramping muscles.\n* **Avoid triggers:** Steer clear of dairy, caffeine, spicy or greasy foods, and heavy meals until you feel better.\n\n*Notice: If you are experiencing sharp, severe, or worsening abdominal pain, persistent vomiting, or a high fever, please seek guidance from a doctor.*",
        "I am so sorry you have this tummy discomfort today. Stomach issues can make you feel incredibly weak and nauseous. \n\nLet's try a gentle acupressure and breathing step to help quiet the nausea:\n* Find the **P6 point** (three finger-widths down from your wrist crease, between the two tendons). Gently press and hold this point for 2 minutes while taking slow, deep abdominal breaths.\n* Lie on your left side, as this natural anatomical position can help ease acid reflux and digestion.\n\nAre you experiencing cramping, mild nausea, or general bloating? Sharing details helps me guide you.",
        "Dealing with stomach pain or nausea is highly draining, and I want to support you through it. \n\nHere are some gentle guidelines to help you cope:\n* Sip warm peppermint or chamomile tea slowly. The natural oils can help relax intestinal muscles.\n* Wear loose, comfortable clothing to avoid putting pressure on your abdomen.\n* Rest in a semi-reclined position rather than lying completely flat, which helps prevent indigestion from rising.\n\nPlease monitor your symptoms closely. If the pain is localized and sharp, or if you can't keep liquids down, it's best to consult a medical practitioner."
    ],
    "fever": [
        "Fever, congestion, and chills are your body's natural, brave way of fighting off an infection, but they can leave you feeling incredibly weak and achy. I'm so sorry you're sick.\n\nHere is how you can support your body's recovery process:\n* **Absolute rest:** Your body needs energy to heal. Stay in bed and avoid physical strain.\n* **Abundant hydration:** Drink plenty of water, herbal teas, or electrolyte fluids to replace lost moisture.\n* **Cool down gently:** Use a damp washcloth on your forehead and wear light, breathable clothing.\n\n*Notice: Please consult a medical practitioner if your fever exceeds 103°F (39.4°C), lasts more than 3 days, or is accompanied by difficulty breathing, chest pain, or a severe sore throat.*",
        "Feeling feverish or sick with flu-like symptoms is highly draining and uncomfortable. Please hear me: **your body is working incredibly hard to protect you right now.** \n\nTo keep yourself as comfortable as possible:\n* Sip warm, clear broths or hot water with a slice of lemon and honey to soothe your throat and thin out congestion.\n* Take a lukewarm sponge bath or place a damp cloth on the back of your neck to help lower your skin temperature comfortably.\n* Wrap yourself in light layers so you can easily adjust if you start shivering or sweating.\n\nWhat is your current temperature, and are you experiencing other symptoms like a cough or body aches?",
        "I'm really sorry you are dealing with a fever and sickness today. It is completely natural to feel exhausted when your immune system is in high gear. \n\nHere is how you can support your recovery today:\n* Rest completely in a quiet, comfortable space.\n* Avoid cold showers or ice packs, as they can cause shivering, which actually raises your core temperature. Lukewarm comfort is best.\n* Focus on small, light meals if you have an appetite, but prioritize fluids above all else.\n\nMake sure to seek professional medical advice if your fever is persistent, or if you experience shortness of breath, a stiff neck, or extreme dizziness."
    ],
    "medications": [
        "When exploring medications, it is always essential to seek personalized advice from a doctor or licensed pharmacist. Here is a helpful guide to common over-the-counter options:\n\n* **Acetaminophen (Paracetamol/Tylenol):** Highly effective for relieving headaches, general body aches, and reducing fevers. *Crucial: Never exceed 4000mg in 24 hours to avoid severe liver damage, and do not combine with other products containing acetaminophen.*\n* **Ibuprofen (Advil/Motrin):** An NSAID that reduces swelling, muscle soreness, joint pain, and inflammation. *Crucial: Always take with food or milk to protect your stomach lining.*\n* **Aspirin:** Used for pain and heart health under guidance. *Never give aspirin to children or teenagers due to the risk of Reye's syndrome.*\n* **Melatonin:** A hormone supplement used short-term to help regulate sleep cycles.\n\nAre you looking up warnings or usage guidelines for a specific medication, or would you like to search our live openFDA database in the Medication Guide tab below?",
        "For mild pain, muscle aches, or fever, **Acetaminophen** and **Ibuprofen** are the most common standard choices, but they function differently in your body. \n\n* **Ibuprofen** is an anti-inflammatory (NSAID) and is excellent for swelling, sprains, or joint stiffness, but must be taken with food.\n* **Acetaminophen** acts directly on pain pathways in the brain to block pain signals and reduce fevers, making it gentle on the stomach but crucial to monitor for liver safety.\n\nAlways read the packaging labels carefully, avoid mixing multiple multi-symptom cold medications, and talk to a professional if you take other prescriptions daily."
    ],
    "login_help": [
        "To configure direct Google OAuth sign-in, a Google Client ID must be set in the system environment. \n\nHowever, **I have made testing incredibly easy for you!** \n\nYou can instantly log in, bypass any authentication prompts, and explore all premium profile features (like dashboards, user profile menus, and saved records) by clicking the custom **'Demo Log'** button in the sign-in modal. It will immediately simulate a highly premium, successful login experience!",
        "Having trouble setting up Google Sign-in? Direct Google Auth requires registering official API credentials. \n\nTo bypass this and see exactly how the application behaves for an active, logged-in user, simply open the login modal and click the **'Demo Log'** button. This will instantly activate the personalized user dashboard and profile features!"
    ],
    "wellness_hub": [
        "Our Health & Wellness Resources Hub is designed to empower you with excellent tools! Scroll down just below this chat window to explore:\n\n* **Health Articles:** Read curated guides on mental resilience, diet, and fitness.\n* **Symptom Checker:** Select symptoms or type in your own custom ailments to compile an instant severity index.\n* **Medication Guide:** Search offline drug sheets or tap directly into the live United States openFDA clinical database!\n* **Wellness Tips:** Access quick-read guidelines and boxes for box breathing.\n* **Research & Science:** Search clinical publications and trials.\n\nWhich of these interactive tools would you like me to guide you through first?",
        "You can easily access our comprehensive Health Resources Hub right below our chat window! It features:\n\n* An **Interactive Symptom Checker** where you can select or type in custom symptoms.\n* A **Medication Guide** with complete offline sheets and full integration with the live United States openFDA API.\n* Structured **Wellness Tips** and articles covering mindfulness, sleep, and physical fitness.\n* A **Research & Science** tab containing searchable clinical papers.\n\nIs there a specific wellness tool or article you would like me to help you locate?",
        "Our wellness dashboard is ready to support you! Simply scroll down to use the **Symptom Checker** for risk assessments, browse the **Medication Guide** to look up common drug safety protocols, or explore **Wellness Tips** for breathing exercises. \n\nLet me know if you would like me to explain how any of these specific tabs work!"
    ],
    "gratitude": [
        "You are so very welcome! It is my absolute pleasure to be here for you. \n\nRemember, taking care of your mental and physical health is a continuous journey, and **you are doing a wonderful job.** Please take gentle care of yourself today, and reach out whenever you need support.",
        "It is my absolute pleasure! I am always here for you, 24/7, whenever you need a listening ear, a quiet space to breathe, or wellness guidance. \n\nI believe in you. Have a beautiful, peaceful rest of your day!",
        "Anytime! I am really glad we could talk through this together. Please don't hesitate to open a chat whenever you want to vent or need a bit of comfort. Take care!"
    ],
    "goodbye": [
        "Goodbye! Please take gentle, compassionate care of yourself today. \n\nI will be right here whenever you need me next. Breathe deep, and be kind to your mind.",
        "Bye for now! Wishing you a peaceful, quiet, and restful day ahead. \n\nRemember that you are doing great, and you deserve gentleness. Speak soon!",
        "See you! Feel free to start a new conversation whenever you are ready. I am always in your corner. Take care!"
    ],
    "sickness_symptoms": [
        "When you are dealing with symptoms of sickness, it is completely natural to feel anxious or worried. Identifying what you are feeling is the first step toward recovery.\n\n* For **mild symptoms** like a runny nose, mild congestion, or fatigue, the most effective solutions are simple, supportive care: deep rest, abundant hydration, and comforting warm fluids.\n* For **moderate symptoms** like a persistent cough, digestive discomfort, or body aches, consider consulting a healthcare professional or trying targeted over-the-counter relief.\n* For **severe symptoms** like chest pain, high fever, or breathing difficulties, please seek immediate medical care.\n\nCan you share a little more about what specific symptoms you are experiencing? You can also type them into our custom **Symptom Checker** below to generate an index report!",
        "Experiencing symptoms of an illness can be highly exhausting, both physically and emotionally. Standard clinical solutions always prioritize hydration, rest, and targeted symptom relief under professional advice.\n\nTo help you get the most accurate guidance, I highly recommend scrolling down to our **Interactive Symptom Checker** tab, where you can select or type in any symptoms you have to receive an immediate severity analysis and tailored instructions."
    ],
    "chronic_serious_illness": [
        "I hear you, and I want to pause and say: **I am so deeply sorry that you are carrying the immense weight of a serious diagnosis like this.** Navigating something as challenging as cancer, diabetes, or chronic illness takes a profound physical and emotional toll, and it is completely natural to feel overwhelmed, anxious, or exhausted. \n\nYour feelings are 100% valid, and you never have to face this alone. Alongside the care of your oncology/medical team, here are some supportive steps we can explore together today:\n* **Research Hub & Science Matching**: Scroll down to our **Research & Science** tab. We can automatically search active, recruiting clinical trials specifically matching the chronic conditions listed on your Health Card.\n* **Stateful Symptom Tracking**: Track day-to-day changes in our **Symptom Checker** to keep an active screening log to share with your clinicians.\n* **Mindfulness & Calm**: Try our voice-guided **Box Breathing Player** under the Wellness tab to help soothe your nervous system and release emotional tension.\n\nI am right here with you. How are you holding up emotionally today? Please let me know how I can best support you in this moment.",
        "Thank you for sharing this with me. Please know that **my thoughts are with you as you navigate this diagnosis.** Hearing terms like cancer or other chronic illnesses can be highly frightening, and I want to offer you a deeply warm, safe, and supportive space.\n\nWhile continuing to work closely with your medical specialists, it can be helpful to maintain a clear sense of control over your day-to-day health metrics:\n* Use our **Pill Organizer** tab to build out your daily dosage schedule so you never miss a dose.\n* Synced wearables in our **Vitals tab** can help you keep a close eye on your resting heart rate and sleep quality.\n* Explore the **Research tab** to find cutting-edge clinical trials that could offer fresh avenues of treatment.\n\nWe can take this completely at your own pace. Would you like to talk about how you are managing your symptoms today, or simply discuss some gentle ways to help comfort your mind and body?"
    ]
}

def match_symptom_knowledgebase(msg):
    # Eyes Burning / Dry Eyes / Irritation
    if re.search(r'\b(eyes?|ocular)\b.*\b(burn(ing)?|dry(ness)?|red(ness)?|itch(y|ing)?|strain(ed)?|water(y|ing)?|sore)\b|\b(burn(ing)?|dry(ness)?|red(ness)?|itch(y|ing)?|strain(ed)?|water(y|ing)?|sore)\b.*\b(eyes?|ocular)\b|\b(eyes?\s*burn|burn\s*eyes?)\b', msg):
        return (
            "👁️ **Symptom: Eye Burning, Strain, or Irritation**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Burning, dry, or red eyes are commonly caused by eye strain (long screen hours), seasonal allergies (allergic conjunctivitis), dry eye syndrome, or contact lens irritation.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Apply a Cool Compress:** Place a clean, damp cloth soaked in cool water over closed eyes for 5-10 minutes to soothe inflammation.\n"
            "* **Rest Your Eyes (20-20-20 Rule):** Every 20 minutes of screen time, look at an object 20 feet away for at least 20 seconds.\n"
            "* **Hydration & Humidity:** Drink plenty of water and use a room humidifier to protect the ocular tear film.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Artificial Tears (Lubricating Eyedrops):** Use drops containing **Carboxymethylcellulose** or **Polyethylene Glycol** 4-6 times daily to restore tear volume. *Warning: Prefer preservative-free drops if using frequently.*\n"
            "* **Antihistamine Eyedrops:** For allergy-induced burning, use **Ketotifen** eyedrops twice daily to block histamine. *Do not use decongestant red-relief drops (like tetrahydrozoline) long-term as they cause rebound redness.*\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Seek immediate medical attention if you experience severe eye pain, changes in your vision (blurry or double vision), extreme sensitivity to light, or thick yellow/green discharge (which suggests bacterial pink eye)."
        )

    # Chest Pain / Palpitations
    if re.search(r'\b(chest|heart|cardiac)\b.*\b(pain(ful)?|tight(ness)?|pressure|racing|palpitations?|squeez(ing)?|hurt(s)?|heavy|heaviness)\b|\b(pain(ful)?|tight(ness)?|pressure|racing|palpitations?|squeez(ing)?|hurt(s)?|heavy|heaviness)\b.*\b(chest|heart|cardiac)\b', msg):
        return (
            "🚨 **CRITICAL SYMPTOM ALERT: Chest Pain or Tightness**\n\n"
            "### ⚠️ 1. EMERGENCY MEDICAL NOTICE\n"
            "**Chest pain, pressure, tightness, or heart palpitations can indicate a life-threatening cardiac emergency (such as a heart attack or angina).**\n\n"
            "### 2. What You Must Do Immediately\n"
            "* **Call Emergency Services (911 or your local emergency number) immediately.**\n"
            "* Do not attempt to drive yourself to the hospital.\n"
            "* Sit down, stay calm, and loosen any tight clothing around your neck.\n"
            "* If you have prescribed Nitroglycerin, use it as directed.\n"
            "* **Do not self-medicate or take at-home treatments** without direct emergency dispatcher instructions."
        )

    # Shortness of Breath
    if re.search(r'\b(breath(ing|e)?|shortness|inhale|exhale|lungs?)\b.*\b(difficult(y|ies)?|trouble|short(ness)?|wheez(ing)?|tight(ness)?|can\'t|restricted|hard)\b|\b(difficult(y|ies)?|trouble|short(ness)?|wheez(ing)?|tight(ness)?|can\'t|restricted|hard)\b.*\b(breath(ing|e)?|shortness|inhale|exhale|lungs?)\b', msg):
        return (
            "🫁 **CRITICAL SYMPTOM: Shortness of Breath or Wheezing**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Difficulty breathing or wheezing is a high-risk symptom often associated with asthma flare-ups, bronchitis, severe allergic reactions (anaphylaxis), pneumonia, or anxiety hyperventilation.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Sit Upright:** Do not lie flat down. Lean forward slightly, resting your elbows on a table.\n"
            "* **Pursed-Lip Breathing:** Inhale slowly through your nose for 2s, purse your lips, and exhale slowly for 4s to expand bronchial airways.\n"
            "* **Stay Calm:** Rapid, shallow breathing from anxiety makes ventilation harder.\n\n"
            "### 3. What Medicines to Take (OTC & Rx Options)\n"
            "* **Rescue Inhaler (Albuterol):** If you have diagnosed asthma, administer 2 puffs of your prescribed **Albuterol bronchodilator** immediately.\n"
            "* **Antihistamines:** If breathing difficulty is paired with hives/swelling (mild allergy), an oral antihistamine like **Diphenhydramine (Benadryl)** may be used under strict supervision.\n\n"
            "### ⚠️ 4. When to Seek Emergency Care\n"
            "Go to the nearest emergency room immediately if you cannot speak in full sentences, your lips or fingernails look blue/gray (cyanosis), you are wheezing severely, or you experience chest pain."
        )

    # Sore Throat
    if re.search(r'\b(throat|swallow(ing)?|tonsils?)\b.*\b(sore(ness)?|pain(ful)?|hurt(s)?|scratchy|swollen|infection)\b|\b(sore(ness)?|pain(ful)?|hurt(s)?|scratchy|swollen|infection)\b.*\b(throat|swallow(ing)?|tonsils?)\b', msg):
        return (
            "🔥 **Symptom: Sore Throat or Painful Swallowing**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Sore throats are primarily caused by viral infections (like the common cold or flu) or bacterial infections (like Strep throat).\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Saltwater Gargle:** Mix 1/2 teaspoon of salt in a glass of warm water. Gargle and spit it out 3-4 times daily to draw out excess fluid and reduce throat swelling.\n"
            "* **Honey & Warm Fluids:** Sip warm water or chamomile tea mixed with honey. Honey acts as a natural demulcent to coat and calm the throat lining.\n"
            "* **Use a Humidifier:** Cool mist humidifiers prevent throat membranes from drying out overnight.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Pain Relievers:** Take **Ibuprofen (Advil)** 200-400mg every 6 hours with food to block throat inflammation, or **Acetaminophen (Tylenol)** 500mg every 6 hours for general throat pain.\n"
            "* **Anesthetic Lozenges:** Use throat lozenges containing **Benzocaine** or **Pectin** to temporarily numb throat nerves.\n"
            "* **Antibiotics warning:** *Never take left-over antibiotics. Antibiotics do not cure viral sore throats; they are only effective for bacterial Strep, which must be officially diagnosed and prescribed by a doctor.*\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Consult a practitioner immediately if you have extreme difficulty breathing, inability to swallow your own saliva (drooling), a high fever (>101°F) without cold symptoms (signs of Strep), or a stiff neck."
        )

    # Earache
    if re.search(r'\b(ear(s)?|ear canal)\b.*\b(ache|pain|hurt(s)?|ring(ing)?|tinnitus|clogged|blocked|infection|fluid)\b|\b(ache|pain|hurt(s)?|ring(ing)?|tinnitus|clogged|blocked|infection|fluid)\b.*\b(ear(s)?|ear canal)\b', msg):
        return (
            "👂 **Symptom: Earache, Ringing, or Clogged Ears**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Ear pain is commonly caused by middle ear infections (otitis media), sinus pressure blockages, excessive earwax buildup, or fluid trapping (swimmer's ear).\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Warm Compress:** Hold a warm damp compress against the affected ear for 10-15 minutes to soothe thumping pain.\n"
            "* **Elevated Sleeping:** Keep your head elevated on extra pillows to assist ear fluid drainage.\n"
            "* **Never Insert Objects:** *Never use cotton swabs (Q-tips), keys, or clips inside your ear canal, as they push earwax deeper and risk rupturing the eardrum.*\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Systemic Pain Relief:** Take **Ibuprofen** 400mg (NSAID) to reduce ear canal swelling, or **Acetaminophen** 500mg for ear pain relief.\n"
            "* **Sinus Decongestants:** If the earache is due to sinus pressure, oral decongestants like **Pseudoephedrine (Sudafed)** help open the Eustachian tube.\n"
            "* **Drops Warning:** *Do not use OTC eardrops if you suspect a ruptured eardrum (drainage/pus present).*\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Consult an ENT specialist if you notice fluid, blood, or pus draining from the ear, experience sudden hearing loss, vertigo/severe dizziness, or if the earache lasts longer than 48 hours."
        )

    # Dizziness
    if re.search(r'\b(dizzy|dizziness|lightheaded|lightheadedness|vertigo|faint(ing|ed)?|room\s*spinning|spinning\s*head|head\s*spinning)\b', msg):
        return (
            "🌀 **Symptom: Dizziness, Lightheadedness, or Vertigo**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Dizziness or vertigo can stem from dehydration, a sudden drop in blood pressure (orthostatic hypotension), low blood sugar, inner ear imbalances, or side effects from medications.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Sit or Lie Down Immediately:** If you feel the room spinning, sit or lie down immediately to prevent falling or fainting.\n"
            "* **Hydration & Glucose:** Drink a large glass of water or sip fruit juice to raise blood sugar and volume levels.\n"
            "* **Rise Slowly:** Avoid sudden movements. When waking up, sit on the edge of the bed for 1-2 minutes before standing.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Motion Sickness Remedies:** For inner ear vertigo, short-term antihistamines like **Meclizine** or **Dimenhydrinate (Dramamine)** can calm vestibular receptors.\n"
            "* **Stay hydrated:** Use **Oral Rehydration Salts (ORS)** to balance sodium/potassium ratios.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Seek emergency medical services immediately if your dizziness is accompanied by sudden weakness or numbness on one side of your body, difficulty speaking or slurred speech, chest pain, or a severe headache (stroke warning signals)."
        )

    # Urinary Burning
    if re.search(r'\b(urin(e|ary|ate|ating)?|pee(ing)?|bladder|micturition)\b.*\b(burn(s|ing)?|pain(ful)?|hurt(s)?|blood|frequent|infection|uti)\b|\b(burn(s|ing)?|pain(ful)?|hurt(s)?|blood|frequent|infection|uti)\b.*\b(urin(e|ary|ate|ating)?|pee(ing)?|bladder|micturition)\b|\b(uti|dysuria)\b', msg):
        return (
            "🚽 **Symptom: Urinary Burning, Painful Urination, or UTI**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Painful urination is most commonly caused by a bacterial Urinary Tract Infection (UTI), urethritis, or bladder inflammation.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Flush Out with Water:** Drink massive amounts of water (8-10 glasses daily) to actively flush bacteria from your urinary tract.\n"
            "* **Unsweetened Cranberry Juice:** High-quality unsweetened cranberry juice contains compounds that help prevent bacteria from adhering to bladder walls.\n"
            "* **Avoid Irritants:** Avoid caffeine, alcohol, spicy foods, and carbonated beverages, which irritate the bladder lining.\n\n"
            "### 3. What Medicines to Take (OTC & Rx Options)\n"
            "* **Symptom Pain Relief:** Take **Phenazopyridine (Azo)** 95mg 3 times daily to anesthetize the urinary tract lining, relieving burning pain instantly. *Caution: This will turn your urine a bright orange/red color, which is harmless, and it does NOT cure the infection.*\n"
            "* **Requires Prescription Antibiotics:** *UTIs cannot be fully cured by home remedies or OTC pain relievers. You must see a doctor to obtain a targeted course of antibiotics (like Nitrofurantoin or Bactrim).*\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Seek immediate medical care if you develop lower back or side pain (flank pain), fever, chills, nausea, or vomiting, as these are critical signs that the infection has spread to your kidneys."
        )

    # Dry Skin and Chapped Lips (Precedence Fix - placed before Skin Rash)
    if re.search(r'\b(dry\s*skin|chapped\s*lips?|flak(y|ing)\s*skin|skin\s*dry(ness)?|dry\s*face|dry\s*patches?|skin\s*peel(ing)?)\b', msg):
        return (
            "🧴 **Symptom: Dry Skin, Flaking, or Chapped Lips**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Dry skin (xerosis) and chapped lips are caused by a compromised skin lipid barrier. Triggers include dry winter air, hot showers, harsh soaps, dehydration, or wind exposure.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Limit Hot Showers:** Shower in lukewarm water for no more than 10 minutes, as hot water strips natural skin oils.\n"
            "* **Apply Moisturizer Immediately:** Apply thick moisturizing cream within 3 minutes of exiting the shower to lock in surface hydration.\n"
            "* **Use a Humidifier:** Keep a cool-mist humidifier running in your bedroom to prevent environmental evaporation.\n\n"
            "### 3. What Medicines & Topicals to Use (OTC Options)\n"
            "* **Barrier Creams (For Dry Skin):** Use thick creams containing **Ceramides**, **Hyaluronic Acid**, or **Colloidal Oatmeal** (e.g., CeraVe/Aveeno) to repair the skin barrier.\n"
            "* **Ointments (For Severe Dryness/Chapped Lips):** Apply **White Petrolatum** (e.g., Vaseline/Aquaphor) to create a protective physical seal.\n"
            "* **Mild Cleansers:** Switch to non-foaming, fragrance-free soap substitutes.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Consult a dermatologist if your dry skin cracks and starts bleeding, shows signs of localized infection (swelling, warmth, yellow crusting), or is accompanied by severe, sleep-disrupting itchiness."
        )

    # Skin Rash
    if re.search(r'\b(skin|rash|hives|bumps?|eczema|bites?)\b.*\b(itch(y|ing)?|red(ness)?|swollen|irritat(ed|ion)|dry(ness)?)\b|\b(itch(y|ing)?|red(ness)?|swollen|irritat(ed|ion)|dry(ness)?)\b.*\b(skin|rash|hives|bumps?|eczema|bites?)\b', msg):
        return (
            "🧴 **Symptom: Skin Rash, Itching, or Hives**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Skin rashes and itching are commonly caused by contact dermatitis (allergen/soap contact), eczema flare-ups, insect bites, or histamine reactions (hives).\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Cool Compress:** Place a cold, damp cloth on the rash to reduce swelling and calm the urge to scratch.\n"
            "* **Oatmeal Bath:** Take a lukewarm bath mixed with colloidal oatmeal to soothe sensitive skin.\n"
            "* **Mild Soaps:** Avoid scrubbing, and use only fragrance-free, hypoallergenic cleansers.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Topical Corticosteroid:** Apply **Hydrocortisone Cream 1%** twice daily to block local skin inflammation and stop itching.\n"
            "* **Oral Antihistamines:** For systemic hives or intense itching, take **Cetirizine (Zyrtec)** 10mg daily (non-drowsy) or **Diphenhydramine (Benadryl)** 25mg at bedtime (causes drowsiness).\n"
            "* **Moisturizers:** Use rich ceramide-based ointments to restore the skin barrier.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Seek emergency services immediately if your rash is accompanied by swelling of your lips, face, or throat, difficulty breathing or wheezing (signs of life-threatening anaphylaxis), or if the rash spreads rapidly and blisters."
        )

    # Toothache
    if re.search(r'\b(tooth|teeth|dental|gums?)\b.*\b(pain(ful)?|ache|hurt(s)?|swollen|bleed(ing)?|sore)\b|\b(pain(ful)?|ache|hurt(s)?|swollen|bleed(ing)?|sore)\b.*\b(tooth|teeth|dental|gums?)\b', msg):
        return (
            "🦷 **Symptom: Toothache or Dental Pain**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Tooth pain is primarily caused by tooth decay (cavities), root infections, cracked teeth, gum disease, or dental abscesses.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Warm Saltwater Rinse:** Rinse your mouth with warm saltwater (1/2 teaspoon salt in a glass) to clean food debris and disinfect the area.\n"
            "* **Cold Compress:** Apply a cold compress or ice pack to the outside of your cheek for 15 minutes to reduce swelling and numb thumping pain.\n"
            "* **Avoid Extreme Temperatures:** Avoid very hot, cold, or highly acidic food/drinks.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Pain & Inflammation Relief:** Take **Ibuprofen (Advil)** 400mg every 6 hours (highly effective for dental pulp swelling), or alternate with **Acetaminophen (Tylenol)** 500mg.\n"
            "* **Topical Anesthetic:** Apply a tiny dab of **Benzocaine Gel 20% (Orajel)** directly to the gum/tooth area for short-term numbing.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Go to a dentist or emergency room immediately if you have swelling in your jaw, cheek, or neck, fever, or difficulty swallowing, as these are critical signs of a spreading facial abscess infection."
        )

    # Constipation
    if re.search(r'\b(constipat(ion|ed)|hard\s*stool|infrequent\s*bowel|poop\s*hard|can\'t\s*poop)\b', msg):
        return (
            "🥬 **Symptom: Constipation or Bloating**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Constipation is generally caused by lack of dietary fiber, insufficient hydration, low physical activity, or side effects from specific medications.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Abundant Water:** Drink 8-10 tall glasses of water daily, as dehydration forces the colon to absorb extra water, hardening stool.\n"
            "* **Fiber Intake:** Eat high-fiber foods such as prunes, apples, oats, and leafy greens.\n"
            "* **Gentle Movement:** Take a brisk 20-minute walk to stimulate bowel motility.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Fiber Supplements (Bulk-forming):** Take **Psyllium Husk (Metamucil)** daily with a full glass of water. *Warning: You must drink plenty of fluids, otherwise it can worsen constipation.*\n"
            "* **Osmotic Laxatives:** For gentle relief, use **Polyethylene Glycol 3350 (MiraLAX)** or **Magnesium Hydroxide (Milk of Magnesia)** to draw water back into the colon.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Consult a practitioner immediately if you experience severe abdominal pain, persistent vomiting, blood in your stool, or have not had a bowel movement for more than a week."
        )

    # Diarrhea
    if re.search(r'\b(diarrhea|watery\s*stool|watery\s*poop|loose\s*stool|stomach\s*flu|food\s*poisoning)\b', msg):
        return (
            "💧 **Symptom: Diarrhea or Loose Stools**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Diarrhea is commonly triggered by food poisoning (bacterial toxin), viral gastroenteritis (stomach flu), or food intolerances.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Hydration & Electrolytes:** The absolute priority is replacing lost fluids. Drink water mixed with **Oral Rehydration Salts (ORS)** or diluted sports drinks.\n"
            "* **Eat Bland Foods (BRAT Diet):** Eat simple foods like Bananas, Rice, Applesauce, and Toast. These are low-fiber, high-starch, and help bind your stool.\n"
            "* **Avoid Irritants:** Steer clear of dairy, high-fat, greasy, or highly sugary foods, which accelerate bowel movements.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Anti-diarrheal Agent:** For quick control, take **Loperamide (Imodium)** 2mg. *Warning: Do NOT take Loperamide if you have a high fever, severe stomach cramps, or bloody stools, as it traps the bacteria in your gut.*\n"
            "* **Bismuth Subsalicylate (Pepto-Bismol):** Acts as a mild antimicrobial and calms intestinal cramping.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Consult a doctor immediately if you have signs of severe dehydration (extreme thirst, dry mouth, dark/no urine), a high fever (>102°F), bloody or black tarry stools, or if diarrhea lasts longer than 48 hours."
        )

    # Cough
    if re.search(r'\b(cough(ing|ed)?|dry\s*cough|wet\s*cough|congestion|coughing\s*up|expectorant|cough\s*syrup)\b', msg):
        return (
            "🗣️ **Symptom: Cough or Mucus Congestion**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "A dry cough is usually caused by throat irritation, asthma, or viral colds, while a wet (productive) cough helps clear mucus from the lungs (bronchitis).\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Steam Inhalation:** Inhale steam from a hot shower or a bowl of hot water to loosen sticky phlegm.\n"
            "* **Honey demulcent:** Take 1-2 teaspoons of natural honey before bed to coat throat receptors and suppress tickles. *Never give honey to children under 1 year old.*\n"
            "* **Hydration:** Drink plenty of warm water or herbal tea to naturally thin out mucus.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **For Dry Cough (Suppressant):** Use **Dextromethorphan (Robitussin)** to temporarily calm the cough reflex in the brain.\n"
            "* **For Wet Cough (Expectorant):** Use **Guaifenesin (Mucinex)** to thin and break up mucus, making it easier to cough up and clear your airways.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Seek medical care if you cough up blood or rust-colored phlegm, experience wheezing or shortness of breath, have a high fever, or if the cough persists for more than 3 weeks."
        )

    # Fever
    if re.search(r'\b(fever|high\s*temp(erature)?|body\s*temp|chills|shivering|running\s*a\s*temp)\b', msg):
        return (
            "🌡️ **Symptom: Fever or High Body Temperature**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Fever is your body's natural immunological defense response to fight off viral or bacterial pathogens, but it can leave you feeling deeply depleted and achy.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Complete Rest:** Save all physical energy to support your immune system's recovery.\n"
            "* **Abundant Fluids:** Drink cool water, clear broths, or sports drinks to replace evaporated body fluids.\n"
            "* **Lukewarm Sponge Bath:** Put a cool damp washcloth on your forehead or take a lukewarm sponge bath. *Avoid cold ice baths as they trigger violent shivering, which actually raises your internal temperature.*\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Systemic Fever Reducers:** Take **Acetaminophen (Paracetamol/Tylenol)** 500mg every 6 hours, or **Ibuprofen (Advil)** 400mg every 6 hours with food to safely bring down core body temperature.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Seek guidance from a practitioner if your fever exceeds 103°F (39.4°C), fails to decrease after 3 days of home care, or is accompanied by chest pain, shortness of breath, or a stiff neck."
        )

    # Stiff Neck (Precedence Fix - placed before Muscle/Joint Pain)
    if re.search(r'\b(neck\s*pain|stiff\s*neck|neck\s*tension|neck\s*stiffness|sore\s*neck|neck\s*spasms?)\b', msg):
        return (
            "🧣 **Symptom: Stiff Neck & Muscle Tension**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Acute stiff neck is typically a painful muscle spasm of the trapezius or levator scapulae muscles. Common causes include poor sleeping posture (sleeping 'wrong'), poor desk ergonomics, or heavy lifting.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Contrast Therapy:** Apply a cold pack for 15 minutes (to reduce acute spasm/pain), followed by a warm heating pad or warm shower (to increase blood flow and relax tight fibers).\n"
            "* **Gentle Active Stretching:** Slowly rotate your head side-to-side and tilt your ears toward your shoulders. *Never stretch through sharp, stabbing pain.*\n"
            "* **Ergonomics Check:** Ensure your computer screen is at eye level to prevent 'text neck'.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Oral Anti-inflammatories:** Take **Ibuprofen (Advil)** 400mg with food or **Naproxen Sodium (Aleve)** 220mg twice daily to reduce cervical muscle inflammation.\n"
            "* **Topical Pain Relief Gel:** Apply **Diclofenac Sodium 1% (Voltaren)** gel or **Menthol** pain patches directly over the painful muscle spasm.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Go to the emergency room immediately if your neck stiffness is so severe that you cannot touch your chin to your chest, especially if accompanied by a high fever, severe headache, photophobia (extreme light sensitivity), or confusion (🚨 symptoms of Meningitis)."
        )

    # Foot or Leg Cramps (Charley Horse) (Precedence Fix - placed before Muscle/Joint Pain)
    if re.search(r'\b(leg\s*cramps?|foot\s*cramps?|charley\s*horse|muscle\s*spasms?\s*in\s*(leg|foot|calf|calves)|spasms?\s*in\s*(leg|foot|calf|calves))\b', msg):
        return (
            "🦵 **Symptom: Leg Cramps or Charley Horse**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Leg or foot cramps are sudden, involuntary, painful contractions of one or more muscles, most commonly the calf. Triggers include dehydration, physical overexertion, prolonged sitting/standing, or mineral imbalances (magnesium, potassium, calcium).\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Stretch the Muscle:** Immediately flex your foot upward (toes pointing toward your shin) and hold to stretch the calf muscle and force it to release.\n"
            "* **Heat and Massage:** Apply a warm towel or heating pad to the cramped muscle, then massage it gently to promote blood flow.\n"
            "* **Hydration & Salt:** Sip electrolyte fluids to restore mineral balance.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Electrolytes / Minerals:** Take **Magnesium Citrate** or **Potassium** supplements daily to prevent recurring cramps. *Ensure adequate calcium and hydration intake.*\n"
            "* **Pain Relief:** **Ibuprofen (Advil)** or **Acetaminophen (Tylenol)** can help soothe residual soreness after a severe cramp has passed.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Consult a practitioner immediately if your leg cramp is accompanied by persistent swelling, redness, or warmth in the calf, as these are critical signs of a Deep Vein Thrombosis (DVT - blood clot), or if the cramps are severe and occur constantly."
        )

    # Muscle or Joint Pain
    if re.search(r'\b(muscles?|back|joints?|bod(y|ies)|bones?|neck)\b.*\b(pain(ful)?|aches?|hurt(s)?|sore(ness)?|sprains?|stiff(ness)?)\b|\b(pain(ful)?|aches?|hurt(s)?|sore(ness)?|sprains?|stiff(ness)?)\b.*\b(muscles?|back|joints?|bod(y|ies)|bones?|neck)\b', msg):
        return (
            "💪 **Symptom: Muscle Pain, Joint Pain, or Sprains**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Body aches, sore muscles, and joint stiffness are commonly triggered by local muscle strains, ligament sprains, physical exhaustion, or systemic viral infections.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **R.I.C.E. Protocol (For Sprains/Strains):** \n"
            "  * **Rest:** Avoid placing strain on the painful area.\n"
            "  * **Ice:** Apply cold gel packs wrapped in a towel for 15-20 minutes to reduce local swelling.\n"
            "  * **Compression:** Wrap a elastic bandage firmly but comfortably to support the joint.\n"
            "  * **Elevation:** Keep the painful limb propped up above heart level.\n"
            "* **Warm Baths:** Soak in a warm bath mixed with Epsom salts (magnesium sulfate) to soothe tight muscle fibers.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Anti-inflammatory NSAIDs:** Take **Ibuprofen (Advil)** 400mg or **Naproxen (Aleve)** 220mg with food to block pain and reduce joint swelling.\n"
            "* **Topical Pain Relief:** Apply an OTC topical NSAID gel like **Diclofenac Sodium 1% (Voltaren)** directly to the sore muscle/joint 3-4 times daily.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Consult a practitioner if you cannot bear weight on a joint, see severe localized swelling or deformity, or experience progressive numbness or tingling down your legs (back/nerve issues)."
        )

    # Headache / Migraine / Tension Headache
    if re.search(r'\b(headache|migraine|head\s*pain|throbbing\s*head|temples\s*hurting|tension\s*headache)\b', msg):
        return (
            "🤕 **Symptom: Headache or Migraine**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Headaches can range from tension headaches (muscle tightness, stress, or dehydration) to migraines (throbbing pain, light/sound sensitivity, nausea) and sinus headaches (pressure around eyes/forehead).\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Quiet, Dark Room:** Rest in a cool, dark room to remove visual and auditory triggers, especially for migraines.\n"
            "* **Hydration:** Dehydration is a very common headache trigger; drink a large glass of cool water immediately.\n"
            "* **Cold or Warm Compress:** Place a cold cloth on your forehead for throbbing migraine pain, or a warm heating pad on your neck for tension tightness.\n"
            "* **Acupressure:** Massage the temples or the webbed area between your thumb and index finger (LI4 point) in circular motions.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **For Tension Headaches:** Take **Ibuprofen (Advil)** 400mg or **Naproxen (Aleve)** 220mg with food to block pain inflammation.\n"
            "* **For General Pain:** Take **Acetaminophen (Tylenol)** 500-1000mg. *Warning: Never exceed 4000mg in 24 hours to avoid liver damage.*\n"
            "* **For Migraines:** Take **Aspirin / Acetaminophen / Caffeine combination (Excedrin Migraine)**. Caffeine helps speed up the absorption of pain relievers.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Go to the emergency room immediately if you experience a sudden, extraordinarily severe headache ('thunderclap' headache), a stiff neck with high fever, confusion, difficulty speaking, numbness, or weakness on one side of your body."
        )

    # Nausea / Vomiting / Stomach Upset
    if re.search(r'\b(nausea|nauseous|vomit(ing)?|throw\s*up|puke|upset\s*stomach|motion\s*sickness)\b', msg):
        return (
            "🤢 **Symptom: Nausea or Vomiting**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Nausea and vomiting are protective reflexes triggered by viral gastroenteritis (stomach flu), food poisoning, acid reflux, motion sickness, or specific medication side effects.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Acupressure (P6 Point):** Find the point three finger-widths down from your wrist crease on the inner arm. Press firmly for 2-3 minutes to ease nausea.\n"
            "* **Ginger & Peppermint:** Sip cool ginger ale, warm ginger tea, or peppermint tea. Ginger contains compounds that naturally calm stomach contractions.\n"
            "* **Small, Frequent Sips:** Do not chug fluids. Take small, frequent sips of water or electrolyte fluids to stay hydrated without triggering more vomiting.\n"
            "* **Rest Upright:** Rest in a semi-reclined position. Lying completely flat can worsen acid reflux and nausea.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **For Stomach Irritation:** Take **Bismuth Subsalicylate (Pepto-Bismol)** 30ml to coat the stomach lining and reduce nausea.\n"
            "* **For Motion Sickness:** Take **Dimenhydrinate (Dramamine)** 50mg or **Meclizine** 25mg to calm inner ear vestibular signals.\n"
            "* **Electrolytes:** Use **Oral Rehydration Salts (ORS)** to replenish sodium and potassium lost through vomiting.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Seek immediate medical attention if you cannot keep liquids down for more than 24 hours, notice blood in your vomit (looks like dark coffee grounds), experience high fever, severe headache, a stiff neck, or intense localized abdominal pain."
        )

    # Fatigue / Weakness / Exhaustion
    if re.search(r'\b(fatigue|exhaust(ed|ion)|weak(ness)?|tired|sluggish|no\s*energy|letharg(ic)?|run\s*down)\b', msg):
        return (
            "😴 **Symptom: Fatigue, Extreme Weakness, or Exhaustion**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Persistent fatigue or weakness is a highly common symptom of viral recovery (post-viral fatigue), chronic sleep deprivation, iron deficiency anemia, thyroid disorders (hypothyroidism), vitamin D/B12 deficiencies, or high stress levels.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Prioritize Rest:** Maintain a regular sleep schedule, aiming for 7-9 hours of quality sleep in a dark, quiet room.\n"
            "* **Gentle Movement:** While counterintuitive, a brief 15-minute outdoor walk can boost circulation, oxygenation, and energy levels.\n"
            "* **Proper Hydration:** Mild dehydration is a stealthy cause of mid-day sluggishness; drink 8-10 glasses of water daily.\n"
            "* **Nutritious Snacks:** Avoid high-sugar snacks that cause energy crashes. Choose complex carbohydrates paired with protein (e.g., apple slices with peanut butter).\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Iron Supplements:** Take **Ferrous Sulfate** only if a blood test has officially confirmed iron deficiency anemia. *Take with Vitamin C to increase absorption.*\n"
            "* **Vitamin Supplements:** Take **Vitamin D3** (1000-2000 IU) or **Vitamin B12** daily if your levels are low.\n"
            "* **Coenzyme Q10 (CoQ10):** A supplement that supports mitochondrial energy production.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Consult a physician if your fatigue is accompanied by sudden shortness of breath with minimal physical effort, chest pain, unexplained weight loss, swelling in your legs, or if the weakness persists for more than 3 weeks despite lifestyle improvements."
        )

    # Acid Reflux / Heartburn / Indigestion
    if re.search(r'\b(acid\s*reflux|heartburn|indigestion|acid\s*stomach|gerd|sour\s*taste|burning\s*chest|flatulence)\b', msg):
        return (
            "🔥 **Symptom: Acid Reflux, Heartburn, or Indigestion**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Heartburn occurs when acidic stomach contents flow back up into the esophagus (acid reflux). It is commonly triggered by large meals, fatty/spicy foods, citrus, chocolate, caffeine, alcohol, or lying down too quickly after eating.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Stay Upright:** Do not lie down or bend over for at least 3 hours after a meal.\n"
            "* **Elevate Bed Head:** Prop the head of your bed up by 6 inches using bed risers or a wedge pillow. *Extra regular pillows can bend your neck and increase abdominal pressure, worsening reflux.*\n"
            "* **Avoid Trigger Foods:** Steer clear of onions, garlic, peppermint, tomato sauce, coffee, and carbonated beverages.\n"
            "* **Wear Loose Clothing:** Tight belts or waistbands squeeze your stomach, pushing acid upwards.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **For Immediate Neutralization:** Take **Antacids (Calcium Carbonate / Tums or Rolaids)** for fast, short-term relief.\n"
            "* **For Sustained Relief (H2 Blockers):** Take **Famotidine (Pepcid)** 10-20mg to reduce stomach acid production for up to 12 hours.\n"
            "* **For Frequent Heartburn (PPIs):** Take **Omeprazole (Prilosec)** 20mg once daily 30 minutes before your first meal. *Limit use to a 14-day course unless directed by a doctor.*\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Seek immediate medical attention if you experience difficulty or pain when swallowing (dysphagia), chest pain that radiates to your arm, neck, or jaw, vomiting blood, or if you require daily acid relief for more than 2 weeks."
        )

    # Allergic Reaction / Hay Fever / Mild Allergy
    if re.search(r'\b(allergy|allerg(ic|ies)|hay\s*fever|hives|pollen|itch(y|iness|ing)?\s*eyes|water(y|ing)?\s*eyes|sneez(e|es|ing))\b', msg):
        return (
            "🌸 **Symptom: Allergic Reaction or Hay Fever**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Allergies are your immune system's overreaction to environmental triggers (pollen, dust mites, mold, pet dander) or mild contact triggers, releasing histamines that cause itching, sneezing, watery eyes, and hives.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Reduce Allergen Exposure:** Keep windows closed during high pollen seasons, wash bedding weekly in hot water, and use a HEPA air purifier.\n"
            "* **Wash Off Pollen:** Shower and wash your hair after spending time outdoors to remove clinging allergens.\n"
            "* **Saline Rinses:** Use a saline spray to clear trapped pollen or dust from your nasal passages.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Non-Drowsy Oral Antihistamines:** Take **Fexofenadine (Allegra)** 180mg, **Cetirizine (Zyrtec)** 10mg, or **Loratadine (Claritin)** 10mg daily to block histamines.\n"
            "* **Antihistamine Eyedrops:** For itchy, burning allergy eyes, use **Ketotifen (Zaditor)** drops twice daily.\n"
            "* **Oral Antihistamine for Hives (Drowsy):** Take **Diphenhydramine (Benadryl)** 25mg at night to calm severe itching and sleep.\n"
            "* **Nasal Steroid Sprays:** **Fluticasone Propionate (Flonase)** helps manage severe sneezing and allergic congestion.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "**Seek emergency medical care immediately (and use an Epinephrine auto-injector if prescribed) if you experience signs of a severe allergic reaction (anaphylaxis): swelling of your throat, lips, tongue, or face, difficulty breathing, wheezing, severe dizziness, or a rapid pulse.**"
        )

    # Nasal Congestion / Runny Nose / Sinus Pressure
    if re.search(r'\b(nose|nasal)\b.*\b(stuffy|congest(ed|ion)?|runny|block(ed)?)\b|\b(stuffy|congest(ed|ion)?|runny|block(ed)?)\b.*\b(nose|nasal)\b|\b(congestion|sinus(itis)?)\b', msg):
        return (
            "👃 **Symptom: Nasal Congestion, Runny Nose, or Sinus Pressure**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Nasal stuffiness and running are caused by swollen blood vessels and excess mucus in your nasal passages, typically triggered by viral infections (colds/flus), seasonal allergies, or sinus infections (sinusitis).\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Saline Nasal Sprays & Rinses:** Use an OTC **Saline Nasal Spray** or a **Neti Pot** with distilled or boiled water to flush out mucus and dry allergens.\n"
            "* **Steam Inhalation:** Sit in a hot shower or inhale steam from a bowl of hot water to open up sinus passages.\n"
            "* **Warm Compresses:** Place a warm, damp cloth across your forehead, eyes, and cheeks to ease facial sinus pressure.\n"
            "* **Hydration:** Drink plenty of warm fluids (herbal teas, broths) to thin out mucus secretions.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Nasal Steroid Spray (For Allergy & Sinus swelling):** Use **Fluticasone Propionate (Flonase)** nasal spray daily. *Requires a few days of consistent use to achieve maximum effect.*\n"
            "* **Oral Decongestants (For Stuffy Nose):** Take **Pseudoephedrine (Sudafed)** to constrict nasal vessels. *Caution: Can increase heart rate and blood pressure; do not take close to bedtime.*\n"
            "* **Antihistamines (For Runny Nose & Sneezing):** Take non-drowsy **Loratadine (Claritin)** 10mg or **Cetirizine (Zyrtec)** 10mg.\n"
            "* **Nasal Decongestant Spray:** **Oxymetazoline (Afrin)** spray provides instant relief. *Warning: Do NOT use Afrin for more than 3 consecutive days, as it causes severe rebound congestion (rhinitis medicamentosa).*\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Consult a healthcare professional if your symptoms last longer than 10-14 days without improvement, if you develop a high fever, severe facial/dental pain, vision changes, or swelling around your eyes."
        )

    # Insomnia & Sleep Disturbances
    if re.search(r'\b(insomnia|sleepless(ness)?|can\'t\s*sleep|trouble\s*sleeping|sleep(less|ing)?\s*(issues?|problems?|disturbances?|difficult(y|ies)?))\b', msg):
        return (
            "🛏️ **Symptom: Insomnia & Sleep Disturbances**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Insomnia is characterized by difficulty falling asleep, staying asleep, or waking up too early. It is often caused by stress, high caffeine intake, screen time (blue light), anxiety, or poor sleep habits.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Cold Bedroom Protocol:** Keep your bedroom cool (60-67°F or 15-19°C), dark, and quiet.\n"
            "* **The 4-7-8 Breathing Technique:** Inhale for 4s, hold for 7s, and exhale completely for 8s to calm your nervous system.\n"
            "* **Dim Screens & Lights:** Turn off all phones, computers, and bright lights at least 45-60 minutes before bed.\n"
            "* **Get Out of Bed:** If awake after 20 minutes, get up, go to a dim corner, and read a physical book until sleepy.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Melatonin (0.5mg - 3mg):** A natural hormone supplement. Take 30-60 minutes before bed. *Warning: Best used for short-term adjustments (jet lag or schedule shifts).*\n"
            "* **Diphenhydramine / Doxylamine Succinate:** Antihistamines used as sleep aids (e.g. ZzzQuil/Unisom). *Warning: Limit use to 1-2 nights; daily use quickly builds tolerance and causes next-day drowsiness.*\n"
            "* **Herbal Valerian Root / Chamomile:** Gentle, non-habit-forming natural sleep teas or capsules.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Consult a practitioner if your insomnia lasts longer than 4 weeks, is accompanied by chronic loud snoring or waking up gasping for air (suspected Sleep Apnea), or severely affects your safety during the day."
        )

    # Cold Sores & Fever Blisters (NEW)
    if re.search(r'\b(cold\s*sores?|fever\s*blisters?|herpes\s*labialis|sores?\s*on\s*lips?|blisters?\s*on\s*lips?)\b', msg):
        return (
            "👄 **Symptom: Cold Sores & Fever Blisters**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Cold sores are small, painful blisters that appear around the lips and mouth, caused by the Herpes Simplex Virus Type 1 (HSV-1). They are highly contagious and triggered by stress, sunlight, fatigue, or a weakened immune system.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Keep It Clean & Dry:** Wash the area gently with mild soap and water, then pat dry.\n"
            "* **Cold Compress:** Apply a cool, damp compress or ice wrapped in a towel for 5-10 minutes to reduce throbbing and swelling.\n"
            "* **Prevent Spreading:** *Avoid kissing, sharing cups, lip balms, or towels, and wash your hands immediately after touching the sore to avoid spreading the virus to your eyes or other body parts.*\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Topical Antiviral Cream:** Apply **Acyclovir** or **Docosanol (Abreva)** cream 5 times daily at the very first sign of tingling to shorten healing time.\n"
            "* **Pain Relief & Protection:** Use **Benzocaine** gel for numbing or apply a thin layer of **White Petrolatum** (Vaseline) to prevent cracking.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Seek medical care if the cold sore spreads close to your eyes (ocular herpes is a medical emergency), doesn't heal within 15 days, is accompanied by a severe fever or difficulty swallowing, or if you have a compromised immune system."
        )

    # Canker Sores
    if re.search(r'\b(canker\s*sores?|mouth\s*ulcers?|oral\s*lesions?|sores?\s*in\s*mouth|ulcers?\s*in\s*mouth)\b', msg):
        return (
            "👅 **Symptom: Canker Sores & Mouth Ulcers**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Canker sores (aphthous ulcers) are painful mucosal lesions. Common triggers include localized biting injuries, stress, acidic or spicy foods, and vitamins/iron deficiencies.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Warm Salt-Water Rinse:** Dissolve 1/2 tsp of salt in warm water. Swish and spit 3 times daily to dry out the sore and speed up tissue healing.\n"
            "* **Diet Modification:** Strictly avoid acidic fruits (citrus, pineapple), spicy curries, and sharp foods (chips) that scratch the lesion.\n"
            "* **Chamomile Tea Apply:** Press a damp, cool chamomile tea bag directly onto the sore to reduce local inflammation.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Topical Anesthetic Gel (Benzocaine 20%):** Apply **Benzocaine** gel (e.g., Orajel) directly onto the sore 3-4 times daily to temporarily numb the throbbing pain.\n"
            "* **Antiseptic Oral Rinse:** Rinse with **Hydrogen Peroxide** based mouthwashes (e.g., Colgate Peroxyl) to cleanse the wound and kill bacteria.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Seek medical/dental advice if an ulcer is larger than 1 cm, lasts longer than 14 days without showing signs of healing, causes severe difficulty swallowing liquids, or is accompanied by a high fever."
        )

    # Heart Palpitations
    if re.search(r'\b(palpitations?|heart\s*racing|flutter(ing)?\s*in\s*chest|skipping\s*beats?|irregular\s*heartbeat|pulse\s*pounding)\b', msg):
        return (
            "💓 **Symptom: Heart Palpitations or Chest Fluttering**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Heart palpitations make you aware of your heart beating. They are frequently benign and triggered by stress, caffeine, anxiety/panic attacks, dehydration, or electrolyte deficiencies (low magnesium/potassium).\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **The Cold Water Shock:** Splash freezing cold water on your face or drink a glass of ice-cold water to stimulate the vagus nerve, which slows heart rate.\n"
            "* **Deep Abdominal Breathing:** Focus on long, slow diaphragmatic breaths to reduce stress hormones.\n"
            "* **Electrolyte Rehydration:** Drink 16 oz of water mixed with an electrolyte powder.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Magnesium Glycinate / Citrate:** Taking a magnesium supplement can support normal cardiac muscle contractions. *Always consult a physician before starting supplements if you have kidney disease.*\n"
            "* **Warning against self-medication:** *Never take someone else's beta-blockers or blood pressure pills without a prescription.*\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Palpitations can sometimes indicate a cardiac arrhythmia. Seek emergency medical care immediately if they are accompanied by chest pain, shortness of breath, sudden fainting (syncope), or a resting heart rate over 120 bpm."
        )

    # Bloating and Gas
    if re.search(r'\b(bloat(ed|ing)?|stomach\s*gas|trapped\s*gas|flatulence|gassy|gas\s*pain|abdominal\s*gas)\b', msg):
        return (
            "💨 **Symptom: Stomach Gas & Bloating**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Abdominal bloating is the sensation of a full, swollen stomach, usually caused by trapped gas, digesting high-fiber foods, swallowed air (eating too fast), carbonated beverages, or lactose intolerance.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Warm Herbal Tea:** Sip warm peppermint, ginger, or fennel tea. The natural compounds help relax the intestinal tract wall muscles.\n"
            "* **Dynamic Stretching:** Lie on your back and pull your knees to your chest (the gas relief yoga pose) to naturally help release trapped pockets of gas.\n"
            "* **Gentle Clockwise Massage:** Rub your abdomen gently in circular motions following the path of the colon.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Simethicone (Gas Relief):** Take **Simethicone** 80-125mg chewable tablets after meals to break up gas bubbles in your gut so they pass easier.\n"
            "* **Activated Charcoal:** Take charcoal capsules to absorb gas in the digestive tract.\n"
            "* **Lactase Enzyme (Lactaid):** Take before meals if dairy triggers your gas/bloating.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Consult your physician if bloating is accompanied by severe abdominal pain, persistent vomiting, unexplained weight loss, visible blood in your stool, or an inability to pass gas or stool (suspected bowel obstruction)."
        )

    # Gastritis and Stomach Cramps
    if re.search(r'\b(acidic\s*stomach|stomach\s*cramps?|gastritis|stomach\s*burning|burning\s*stomach|burning\s*in\s*my\s*stomach|belly\s*cramps?)\b', msg):
        return (
            "🥣 **Symptom: Acidic Stomach, Burning, or Cramping**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Burning stomach pain or gastritis is caused by an irritated, inflamed stomach lining. It is often triggered by excess gastric acid, high NSAID usage (like Ibuprofen on an empty stomach), alcohol, or stress.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Avoid Acidic & Irritating Foods:** Stay completely away from caffeine, citrus fruits, vinegar, spicy curries, fried foods, and carbonated beverages.\n"
            "* **Eat Small, Bland Meals:** Consume small portions of plain oatmeal, white rice, bananas, or boiled potatoes to soothe the mucosal lining.\n"
            "* **Drink Cold Milk or Water:** Sip cold water or a small glass of milk (which neutralizes acid temporarily).\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Antacids (Rapid Neutralization):** Chew tablets containing **Calcium Carbonate** (e.g. Tums) for instant, rapid relief.\n"
            "* **H2 Blockers (Reduce Acid Production):** Take **Famotidine (Pepcid)** 10-20mg once daily to block stomach acid production short-term.\n"
            "* **NSAID Warning:** *Avoid taking aspirin, ibuprofen, or naproxen as they directly irritate and damage the stomach lining during gastritis.*\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Seek immediate medical attention if you experience severe, sharp, or sudden stomach pain, vomit blood (or material that looks like dark coffee grounds), have black tarry stools (suggests bleeding), or unexplained weight loss."
        )

    # Red Eye and Pink Eye
    if re.search(r'\b(red\s*eyes?|pink\s*eyes?|bloodshot\s*eyes?|conjunctivitis|eyes?\s*inflamed|swollen\s*eyelids?)\b', msg):
        return (
            "👁️ **Symptom: Red Eyes, Pink Eye, or Conjunctivitis**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Red or bloodshot eyes are caused by expanded blood vessels in the conjunctiva. Triggers include allergies, viral or bacterial infections (pink eye), dry eyes, or dust exposure.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Warm Compress (For Crusting):** If eyelids are stuck shut with crust in the morning, place a warm damp cloth over eyes to melt and gently wipe the build-up.\n"
            "* **Strict Hygiene:** *Pink eye is highly contagious! Wash hands frequently, use separate towels, and discard used contact lenses immediately.*\n"
            "* **Avoid Contacts:** Do not wear contact lenses until the eye redness is completely gone.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Lubricating Eye Drops:** Use preservative-free **Artificial Tears** 4-6 times daily to soothe general ocular redness.\n"
            "* **Antihistamine Eye Drops:** Take drops containing **Ketotifen** for red, itchy eyes triggered by seasonal allergies.\n"
            "* **Warning against Vasoconstrictors:** *Avoid drops like Tetrahydrozoline (Visine) for more than 2 days, as they cause severe rebound blood vessel dilation.*\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Seek immediate medical attention if you experience severe pain inside the eye, vision changes, extreme light sensitivity (photophobia), or thick, yellow/green discharge that keeps returning."
        )

    # Numbness and Tingling
    if re.search(r'\b(numb(ness)?|tingl(ing)?|pins\s*and\s*needles|loss\s*of\s*sensation|limbs?\s*asleep|arm\s*numb|leg\s*numb|foot\s*numb)\b', msg):
        return (
            "⚡ **Symptom: Numbness, Tingling, or Pins & Needles**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Numbness and tingling (paresthesia) is caused by temporary nerve compression (limb 'sleeping') or nerve irritation. Ongoing causes can include vitamin deficiencies (B12), diabetic neuropathy, or a pinched spinal nerve.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Release Compression:** If a limb is asleep, gently shake it, stand up, and walk around to restore circulation and release compressed nerves.\n"
            "* **Nerve Glide Exercises:** Perform slow stretching routines (e.g. neck tilts or hamstring stretches) to release trapped peripheral nerves.\n"
            "* **Check Posture:** Avoid crossed legs or resting on elbows for prolonged periods.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Vitamin B-Complex Supplements:** Supplying **Vitamin B12**, **B6**, and **Folic Acid** helps repair and maintain healthy myelin nerve sheaths.\n"
            "* **NSAIDs (For Pinched Nerves):** Take **Ibuprofen (Advil)** 400mg with food to reduce local swelling around a pinched nerve root.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Sudden numbness can indicate a neurological emergency. Seek immediate emergency care if numbness starts suddenly on one side of your body, is accompanied by facial drooping, weakness in your arm/leg, slurred speech, or confusion (🚨 signs of a Stroke)."
        )

    # Minor Burns and Sunburns
    if re.search(r'\b(minor\s*burns?|sun\s*burns?|burned\s*my\s*skin|first\s*degree\s*burns?|skin\s*burn(ed|ing)?)\b', msg):
        return (
            "☀️ **Symptom: Minor Burn or Sunburn**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Minor burns (first-degree) damage only the outer layer of the skin (epidermis), causing redness, swelling, and localized pain. They are caused by thermal contact (hot liquid/stoves) or UV radiation (sunburn).\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Cool Water Bathing:** Immediately submerge the burn in cool (not freezing) running water for 10-20 minutes. *Never use ice, as it further damages skin cells.*\n"
            "* **Aloe Vera Gel:** Apply pure, alcohol-free Aloe Vera gel to cool, soothe, and moisturize the irritated skin.\n"
            "* **Do Not Pop Blisters:** If small blisters form, do not squeeze or pop them, as they serve as a sterile barrier against infection.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Pain Relief:** Take **Ibuprofen (Advil)** 400mg with food immediately to block inflammatory pain and swelling.\n"
            "* **Protectants:** Apply **Petroleum Jelly (Vaseline)** or **Antibiotic Ointment** (e.g. Neosporin) gently over a non-blistered burn and cover with a sterile, non-stick bandage.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Seek immediate medical care if a burn covers a large area (larger than 3 inches), develops severe large blisters, shows signs of third-degree charring (white, dry, or charred black skin), is on your face, hands, or joints, or shows signs of infection (pus, worsening pain)."
        )

    # Hair Loss & Thinning (NEW)
    if re.search(r'\b(hair\s*loss|balding|hair\s*fall|shedding\s*hair|alopecia)\b|\b(hair)\b.*\b(thin(ning)?|fall(ing)?|loss|shed(ding)?)\b|\b(thin(ning)?|fall(ing)?|loss|shed(ding)?)\b.*\b(hair)\b', msg):
        return (
            "💇 **Symptom: Hair Loss & Thinning**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Hair thinning or excessive shedding (telogen effluvium) is commonly triggered by high physical or emotional stress, nutritional deficiencies (low iron, zinc, or vitamin D), hormonal shifts (thyroid, postpartum), or genetics (androgenetic alopecia).\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Balanced Nutrition:** Ensure an adequate intake of lean proteins, iron, zinc, and healthy fats.\n"
            "* **Gentle Hair Care:** Avoid tight hairstyles, excessive heat styling, chemical treatments, and vigorous wet brushing.\n"
            "* **Scalp Massage:** Massage your scalp daily for 4-5 minutes to increase localized blood circulation to hair follicles.\n\n"
            "### 3. What Medicines & Supps to Take (OTC Options)\n"
            "* **Topical Treatment:** Apply **Minoxidil 2% or 5%** solution or foam directly to the scalp twice daily to stimulate hair regrowth. *Warning: Must be used continuously to maintain results.*\n"
            "* **Supplements:** Take **Biotin**, **Iron** (if deficient), or **Multi-vitamins** containing Zinc and Vitamin D to support follicular health.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Consult a dermatologist if you experience sudden, rapid hair loss in patches (suspected alopecia areata), scalp scaling, redness, intense itching or burning, or if hair loss is accompanied by unexplained fatigue, weight changes, or irregular menstrual cycles."
        )

    # Dry Mouth (Xerostomia) (NEW)
    if re.search(r'\b(dry\s*mouth|xerostomia|lack\s*of\s*saliva|cotton\s*mouth|sticky\s*mouth)\b|\b(mouth|oral|tongue)\b.*\b(dry(ness)?|sticky|cotton)\b|\b(dry(ness)?|sticky|cotton)\b.*\b(mouth|oral|tongue)\b', msg):
        return (
            "💧 **Symptom: Dry Mouth (Xerostomia)**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Dry mouth occurs when salivary glands do not produce enough saliva. It is commonly caused by dehydration, anxiety, breathing through your mouth at night, or side effects from medications (like antihistamines, antidepressants, or decongestants).\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Sip Fluids Frequently:** Drink water or sugar-free fluids throughout the day to keep oral tissues lubricated.\n"
            "* **Chew Sugar-Free Gum:** Chew gum or suck on sugar-free candies containing **Xylitol** to stimulate natural saliva flow.\n"
            "* **Avoid Dehydrators:** Strictly limit caffeine, alcohol, tobacco, and dry, salty, or spicy foods.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Artificial Saliva Substitutes:** Use OTC oral sprays, gels, or rinses containing **Carboxymethylcellulose** (e.g. Biotene) to coat and moisten the mouth.\n"
            "* **Fluoride Care:** Saliva protects teeth from decay. Use a fluoride mouthwash daily to prevent cavities caused by a lack of saliva.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Seek medical/dental advice if dry mouth is accompanied by difficulty swallowing or speaking, painful oral sores, severe tooth decay, or dry eyes and joint pain (which can indicate an autoimmune disorder like Sjögren's Syndrome)."
        )

    # Nail Fungus & Brittle Nails (NEW)
    if re.search(r'\b(nail\s*fungus|brittle\s*nails?|thickened\s*nails?|yellow\s*nails?|fungal\s*nail|onychomycosis)\b', msg):
        return (
            "💅 **Symptom: Nail Fungus & Brittle Nails**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Fungal nail infections (onychomycosis) cause nails to become yellow, thickened, and brittle. Nails can also become brittle due to frequent handwashing, harsh chemicals, or thyroid imbalances.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Keep Nails Trimmed & Dry:** Keep your nails short, clean, and completely dry. Disinfect nail clippers after each use.\n"
            "* **Breathable Footwear:** Wear moisture-wicking socks and shoes that let air circulate to prevent moisture trapping.\n"
            "* **Tea Tree Oil:** Apply diluted tea tree oil to the nail plate, as it has natural antifungal properties.\n\n"
            "### 3. What Medicines to Take (OTC & Rx Options)\n"
            "* **Topical Antifungal Lacquer:** Apply OTC **Undecylenic Acid** or **Tolnaftate** nail solutions daily. *Note: OTC topicals have low cure rates for deep nail bed infections and must be used for months.*\n"
            "* **Requires Prescription Oral Antifungals:** *To fully cure a moderate-to-severe nail infection, a doctor must prescribe oral medicines like Terbinafine (Lamisil) after conducting a nail clipping test.*\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Consult a practitioner if the nail becomes extremely painful, shows signs of bacterial infection in the surrounding skin (redness, pus, severe swelling), or if you have diabetes or a compromised immune system (as minor foot issues can rapidly lead to severe complications)."
        )

    # Red Eye and Pink Eye
    if re.search(r'\b(red\s*eyes?|pink\s*eyes?|bloodshot\s*eyes?|conjunctivitis|eyes?\s*inflamed|swollen\s*eyelids?)\b', msg):
        return (
            "👁️ **Symptom: Red Eyes, Pink Eye, or Conjunctivitis**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Red or bloodshot eyes are caused by expanded blood vessels in the conjunctiva. Triggers include allergies, viral or bacterial infections (pink eye), dry eyes, or dust exposure.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Warm Compress (For Crusting):** If eyelids are stuck shut with crust in the morning, place a warm damp cloth over eyes to melt and gently wipe the build-up.\n"
            "* **Strict Hygiene:** *Pink eye is highly contagious! Wash hands frequently, use separate towels, and discard used contact lenses immediately.*\n"
            "* **Avoid Contacts:** Do not wear contact lenses until the eye redness is completely gone.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Lubricating Eye Drops:** Use preservative-free **Artificial Tears** 4-6 times daily to soothe general ocular redness.\n"
            "* **Antihistamine Eye Drops:** Take drops containing **Ketotifen** for red, itchy eyes triggered by seasonal allergies.\n"
            "* **Warning against Vasoconstrictors:** *Avoid drops like Tetrahydrozoline (Visine) for more than 2 days, as they cause severe rebound blood vessel dilation.*\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Seek immediate medical attention if you experience severe pain inside the eye, vision changes, extreme light sensitivity (photophobia), or thick, yellow/green discharge that keeps returning."
        )

    # Numbness and Tingling
    if re.search(r'\b(numb(ness)?|tingl(ing)?|pins\s*and\s*needles|loss\s*of\s*sensation|limbs?\s*asleep|arm\s*numb|leg\s*numb|foot\s*numb)\b', msg):
        return (
            "⚡ **Symptom: Numbness, Tingling, or Pins & Needles**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Numbness and tingling (paresthesia) is caused by temporary nerve compression (limb 'sleeping') or nerve irritation. Ongoing causes can include vitamin deficiencies (B12), diabetic neuropathy, or a pinched spinal nerve.\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Release Compression:** If a limb is asleep, gently shake it, stand up, and walk around to restore circulation and release compressed nerves.\n"
            "* **Nerve Glide Exercises:** Perform slow stretching routines (e.g. neck tilts or hamstring stretches) to release trapped peripheral nerves.\n"
            "* **Check Posture:** Avoid crossed legs or resting on elbows for prolonged periods.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Vitamin B-Complex Supplements:** Supplying **Vitamin B12**, **B6**, and **Folic Acid** helps repair and maintain healthy myelin nerve sheaths.\n"
            "* **NSAIDs (For Pinched Nerves):** Take **Ibuprofen (Advil)** 400mg with food to reduce local swelling around a pinched nerve root.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Sudden numbness can indicate a neurological emergency. Seek immediate emergency care if numbness starts suddenly on one side of your body, is accompanied by facial drooping, weakness in your arm/leg, slurred speech, or confusion (🚨 signs of a Stroke)."
        )

    # Minor Burns and Sunburns
    if re.search(r'\b(minor\s*burns?|sun\s*burns?|burned\s*my\s*skin|first\s*degree\s*burns?|skin\s*burn(ed|ing)?)\b', msg):
        return (
            "☀️ **Symptom: Minor Burn or Sunburn**\n\n"
            "### 1. Clinical Assessment & Causes\n"
            "Minor burns (first-degree) damage only the outer layer of the skin (epidermis), causing redness, swelling, and localized pain. They are caused by thermal contact (hot liquid/stoves) or UV radiation (sunburn).\n\n"
            "### 2. How to Cure & Relieve (At-Home Steps)\n"
            "* **Cool Water Bathing:** Immediately submerge the burn in cool (not freezing) running water for 10-20 minutes. *Never use ice, as it further damages skin cells.*\n"
            "* **Aloe Vera Gel:** Apply pure, alcohol-free Aloe Vera gel to cool, soothe, and moisturize the irritated skin.\n"
            "* **Do Not Pop Blisters:** If small blisters form, do not squeeze or pop them, as they serve as a sterile barrier against infection.\n\n"
            "### 3. What Medicines to Take (OTC Options)\n"
            "* **Pain Relief:** Take **Ibuprofen (Advil)** 400mg with food immediately to block inflammatory pain and swelling.\n"
            "* **Protectants:** Apply **Petroleum Jelly (Vaseline)** or **Antibiotic Ointment** (e.g. Neosporin) gently over a non-blistered burn and cover with a sterile, non-stick bandage.\n\n"
            "### ⚠️ 4. When to See a Doctor (Red Flags)\n"
            "Seek immediate medical care if a burn covers a large area (larger than 3 inches), develops severe large blisters, shows signs of third-degree charring (white, dry, or charred black skin), is on your face, hands, or joints, or shows signs of infection (pus, worsening pain)."
        )

    return None

def get_intent_candidates(message):
    msg = message.lower()
    
    # 1. Direct Clinical Symptom Knowledgebase Check (highest priority!)
    symptom_response = match_symptom_knowledgebase(msg)
    if symptom_response:
        return "symptom_kbase", [symptom_response]
        
    # 2. Greetings
    if re.search(r'\b(hello|hi|hey|greetings|good morning|good afternoon|howdy|hey there|hi there)\b', msg):
        return "greeting", INTENT_RESPONSES["greeting"]
        
    # Medications (Checked first to prioritize specific drug queries over generic symptoms!)
    if re.search(r'\b(medications?|medicines?|pills?|drugs?|tablets?|capsules?|prescriptions?|dosages?|side\s*effects?|ibuprofen|paracetamol|aspirin|acetaminophen|melatonin|advil|tylenol|cough\s*syrup|painkillers?|antibiotics?|otc)\b', msg):
        if re.search(r'\b(cold|cough|flu|congestion|runny nose|sore throat)\b', msg):
            return "medications_cold", [
                "When looking for **cold and flu medications**, over-the-counter options generally target specific symptoms:\n\n* **Decongestants** (like **Pseudoephedrine** or **Phenylephrine**): Help relieve nasal congestion and stuffy nose.\n* **Antihistamines** (like **Diphenhydramine** or **Cetirizine**): Useful for runny nose, sneezing, and watery eyes.\n* **Cough Suppressants** (like **Dextromethorphan**): Help quiet a dry, hacking cough.\n* **Pain Relievers/Fever Reducers** (like **Paracetamol** or **Ibuprofen**): Help soothe body aches, sore throat, and fever.\n\n*Always check multi-symptom cold products to make sure you do not accidentally double-dose on the same active ingredients. What specific cold symptoms are you hoping to treat today?*"
            ]
        elif re.search(r'\b(headache|migraine|head pain)\b', msg):
            return "medications_headache", [
                "For **headaches**, the primary over-the-counter pain relievers are:\n\n* **Acetaminophen (Paracetamol):** Excellent for general head pain and gentle on the stomach.\n* **Ibuprofen or Naproxen (NSAIDs):** Excellent for throbbing tension headaches as they reduce inflammation.\n* **Combination Pain Relievers** (containing **Aspirin, Acetaminophen, and Caffeine**): Often highly effective for stubborn tension headaches or migraines, as caffeine boosts the pain-relieving effects."
            ]
        elif re.search(r'\b(stomach|nausea|acid|heartburn|tummy)\b', msg):
            return "medications_stomach", [
                "For **stomach aches, acid reflux, or nausea**, standard over-the-counter remedies include:\n\n* **Antacids** (like **Calcium Carbonate / Tums**): Provide rapid relief for heartburn, acid indigestion, and sour stomach.\n* **H2 Blockers or PPIs** (like **Famotidine** or **Omeprazole**): Help reduce stomach acid production for longer-term heartburn relief.\n* **Bismuth Subsalicylate (Pepto-Bismol):** Helps treat nausea, indigestion, upset stomach, diarrhea, and abdominal fullness."
            ]
        return "medications", INTENT_RESPONSES["medications"]

    # Google Login / OAuth FAQ
    if re.search(r'\b(login|log in|signin|sign in|google login|google auth|oauth|401|invalid_client|error 401|register|demo log|bypass|sign up|signup)\b', msg):
        return "login_help", INTENT_RESPONSES["login_help"]
        
    # Capabilities / Who are you
    if re.search(r'\b(who are you|what are you|what can you do|capabilities|help|how to use|features|services)\b', msg):
        return "capabilities", INTENT_RESPONSES["capabilities"]
        
    # Headache
    if re.search(r'\b(headache|migraine|head pain|throbbing head|temples hurting|eye strain)\b', msg):
        return "headache", INTENT_RESPONSES["headache"]
        
    # Stomach
    if re.search(r'\b(stomach|nausea|vomit|indigestion|tummy|bellyache|cramp|diarrhea|acid reflux)\b', msg):
        return "stomach", INTENT_RESPONSES["stomach"]
        
    # Fever / Cold / Flu
    if re.search(r'\b(fever|cold|flu|cough|sore throat|congestion|runny nose|high temp|shivering|chills|sick)\b', msg):
        return "fever", INTENT_RESPONSES["fever"]

    # Anxiety / Panic
    if re.search(r'\b(panic|anxious|anxiety|scared|frightened|heart racing|hyperventilating|can\'t breathe|nervous|worry|stressed|stress|burnout)\b', msg):
        return "anxiety", INTENT_RESPONSES["anxiety"]
        
    # Sleep issues
    if re.search(r'\b(sleep|insomnia|tired|can\'t sleep|wake up|nightmare|exhausted|restless|sleepy)\b', msg):
        return "sleep", INTENT_RESPONSES["sleep"]



    # Chronic / Serious Illnesses (Cancer, Diabetes, Heart Failure, etc.)
    if re.search(r'\b(cancer|tumor|chemo|chemotherapy|leukemia|lymphoma|diabetes|diabetic|heart\s*failure|cardiac\s*arrest|stroke|arthritis|rheumatoid|chronic|oncology|oncologist)\b', msg):
        return "chronic_serious_illness", INTENT_RESPONSES["chronic_serious_illness"]

    # Sickness / Symptoms / Solutions
    if re.search(r'\b(symptoms?|sickness(es)?|illnesses?|diseases?|solutions?|cures?|treatments?|remed(y|ies)|therap(y|ies)|diagnos(is|e|es)|unwell|sickly)\b', msg):
        return "sickness_symptoms", INTENT_RESPONSES["sickness_symptoms"]

    # Wellness Hub Tabs
    if re.search(r'\b(articles|checker|symptom checker|medication guide|wellness tips|research tab|hub|resources tab)\b', msg):
        return "wellness_hub", INTENT_RESPONSES["wellness_hub"]
        
    # Gratitude
    if re.search(r'\b(thank you|thanks|helpful|appreciate|great job|awesome|perfect)\b', msg):
        return "gratitude", INTENT_RESPONSES["gratitude"]
        
    # Goodbye
    if re.search(r'\b(bye|goodbye|see you|good night|exit|quit|talk later)\b', msg):
        return "goodbye", INTENT_RESPONSES["goodbye"]
        
    return None

def filter_repeats(candidates, history):
    past_bot_messages = [h["bot"] for h in history if "bot" in h]
    # Filter candidates that were sent in the last 4 turns to ensure high variety
    filtered = [c for c in candidates if c not in past_bot_messages[-4:]]
    if filtered:
        return filtered
    return candidates

def is_general_followup_needed(message, history):
    # Only trigger generic followups if the conversation is ongoing AND the message is brief and general
    if len(history) < 2:
        return False
    
    words = message.lower().split()
    if len(words) > 6:
        return False
        
    # Check if it has any key terms that deserve a direct sentiment response
    for word in words:
        if word in ["sad", "happy", "bad", "good", "hurt", "pain", "angry", "crying", "scared", "alone", "lonely"]:
            return False
            
    return random.random() > 0.5

def get_response(message, sentiment, severity, history, symptoms=None):
    # 1. Crisis takes absolute priority
    if severity == "crisis":
        return filter_repeats(RESPONSES["crisis"], history)[0]

    # 2. Check for semantic intent matching (Greetings, Google Login FAQ, Symptoms, Medications, Sleep, Anxiety, etc.)
    intent_data = get_intent_candidates(message)
    if intent_data:
        intent_name, candidates = intent_data
        if intent_name == "greeting" and symptoms:
            formatted_syms = " and ".join([s.replace("_", " ") for s in symptoms])
            return f"Hello! I am your AI Health Assistant. I noticed in your recent Symptom Checker run that you were experiencing **{formatted_syms}**. How are you carrying those symptoms today? Did rest help, or do you need a fresh guidance assessment?"
        selected = random.choice(filter_repeats(candidates, history))
        return selected

    # 3. Contextual dialogue / general followup check
    # If the user is having an ongoing chat, and supplies a very brief response, alternate with a conversational prompt.
    if is_general_followup_needed(message, history):
        last_sentiment = history[-1].get("sentiment", "neutral")
        if last_sentiment in ["distressed", "crisis", "negative"]:
            candidates = RESPONSES["followup_distressed"]
        else:
            candidates = RESPONSES["followup_general"]
    else:
        # Match current sentiment pool directly for high-fidelity responses
        if sentiment == "distressed":
            if severity == "high":
                candidates = RESPONSES["distressed_high"]
            else:
                candidates = RESPONSES["distressed_medium"]
        elif sentiment == "negative":
            candidates = RESPONSES["negative"]
        elif sentiment == "positive":
            candidates = RESPONSES["positive"]
        else:
            candidates = RESPONSES["neutral"]

    # Apply strict repetition filtering
    selected = random.choice(filter_repeats(candidates, history))
    return selected
