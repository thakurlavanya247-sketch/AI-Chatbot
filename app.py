import streamlit as st
import os
from groq import Groq

# get API key from environment
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

st.title("My AI Chatbot")

# store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# user input
if prompt := st.chat_input("Ask something..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI response
    chat = client.chat.completions.create(
        messages=st.session_state.messages,
        model="llama-3.1-8b-instant",
    )

    reply = chat.choices[0].message.content

    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
