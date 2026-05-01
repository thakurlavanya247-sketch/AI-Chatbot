import os
from groq import Groq

# ✅ get API key securely from environment
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(" GROQ_API_KEY not set. Please add it as an environment variable.")

# create client
client = Groq(api_key=api_key)

print("🤖 Chat started (type 'exit' to quit)\n")

messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("👋 Chat ended")
        break

    # add user message
    messages.append({"role": "user", "content": user_input})

    try:
        chat = client.chat.completions.create(
            messages=messages,
            model="llama-3.1-8b-instant",
        )

        reply = chat.choices[0].message.content

        print("AI:", reply)

        # store AI reply
        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("❌ Error:", e)