from textblob import TextBlob

def detect_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity < -0.5:
        return "Very Sad", "I'm really sorry you're feeling that way. You're not alone — talking can help."
    elif polarity < 0:
        return "Sad", "It's okay to feel down sometimes. Want to try a calming exercise?"
    elif polarity == 0:
        return "Neutral", "Thanks for sharing. I'm here to listen if you need me."
    elif polarity < 0.5:
        return "Calm", "You seem to be doing okay. Let me know if you'd like any mental health tips."
    else:
        return "Happy", "I'm glad you're feeling good! 😊 Keep it up!"
