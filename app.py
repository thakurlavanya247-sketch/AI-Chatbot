import streamlit as st
import os
from groq import Groq

# 🔐 Get API key from Streamlit secrets
api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

# 🌟 Page config
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# 🎨 Custom CSS (premium look)
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.block-container {
    padding-top: 2rem;
}
.chat-container {
    max-width: 700px;
    margin: auto;
}
.user-msg {
    background-color: #1f2937;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
}
.ai-msg {
    background-color: #111827;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# 🎯 Title
st.markdown("<h1 style='text-align:center;'>🤖 AI Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Ask anything, get smart answers instantly</p>", unsafe_allow_html=True)

# 💬 Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# 📜 Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-msg'>🧑 {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='ai-msg'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

# ✏️ Input
prompt = st.chat_input("Type your message...")

if prompt:
    # show user msg
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Thinking... 🤔"):
        chat = client.chat.completions.create(
            messages=st.session_state.messages,
            model="llama-3.1-8b-instant",
        )

        reply = chat.choices[0].message.content

    # show AI msg
    st.session_state.messages.append({"role": "assistant", "content": reply})

    st.rerun()
