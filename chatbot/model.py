from transformers import pipeline
import re

# Load a lightweight sentiment model
_classifier = None

def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=1
        )
    return _classifier

CRISIS_KEYWORDS = [
    "kill myself", "want to die", "end my life", "suicide", "hurt myself",
    "self harm", "no reason to live", "can't go on", "give up on life"
]

DISTRESS_KEYWORDS = [
    "depressed", "hopeless", "worthless", "alone", "lonely", "can't sleep",
    "anxious", "panic", "scared", "overwhelmed", "exhausted", "numb", "empty"
]

def classify_sentiment(text):
    text_lower = text.lower()

    # Check for crisis first
    if any(kw in text_lower for kw in CRISIS_KEYWORDS):
        return "crisis", "crisis"

    # Check for clear distress keywords
    if any(kw in text_lower for kw in DISTRESS_KEYWORDS):
        return "distressed", "high"

    # Use transformer model for nuanced classification
    try:
        clf = get_classifier()
        result = clf(text)[0][0]
        label = result["label"].lower()
        score = result["score"]

        if label in ["fear", "sadness", "anger"] and score > 0.6:
            severity = "high" if score > 0.85 else "medium"
            return "distressed", severity
        elif label in ["disgust"] and score > 0.6:
            return "negative", "medium"
        elif label in ["joy", "surprise"] and score > 0.5:
            return "positive", "low"
        else:
            return "neutral", "low"
    except Exception:
        # Fallback to keyword matching if model fails
        negative_words = ["sad", "bad", "terrible", "awful", "horrible", "upset", "angry"]
        if any(w in text_lower for w in negative_words):
            return "negative", "medium"
        return "neutral", "low"
