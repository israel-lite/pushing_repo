import streamlit as st
from googletrans import Translator
from datetime import datetime, timedelta

# Initialize translator
translator = Translator()

# Chat history and custom timer
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.now()  # Custom zero-time

st.title(" Python Chatroom with Translation & Timer")

# Choose language
user_language = st.selectbox(
    "Choose your language:",
    ["en", "fr", "es", "de", "ja", "zh-cn", "ha"]
)

# User input
user_msg = st.text_input("Enter your message:")

if st.button("Send") and user_msg:
    # Translate message
    translated_msg = translator.translate(user_msg, dest=user_language).text
    # Calculate custom time (seconds since start)
    custom_time = (datetime.now() - st.session_state.start_time).seconds
    st.session_state.chat_history.append(f"[{custom_time}s] You ({user_language}): {translated_msg}")

# Display chat history
st.subheader("Chat History")
for msg in st.session_state.chat_history:
    st.write(msg)

