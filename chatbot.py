import streamlit as st
from emotion_model import detect_emotion

st.title("🧠 MindMate - Mental Health Support Bot")

user_input = st.text_input("How are you feeling today?")

if user_input:
    emotion, response = detect_emotion(user_input)
    st.markdown(f"**Emotion Detected:** {emotion}")
    st.markdown(f"**Bot Response:** {response}")
