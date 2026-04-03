import ollama

print("🤖 Smart Chatbot (Optimized) started! Type 'exit' to quit.\n")

MAX_HISTORY = 6

conversation = [
    {
        "role": "system",
        "content": """
You are an expert AI tutor.

Rules:
1. Explain simply
2. Use bullet points
3. Give examples
"""
    }
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    conversation.append({"role": "user", "content": user_input})

    # 🧠 Keep only last N messages (IMPORTANT)
    if len(conversation) > MAX_HISTORY:
        conversation = [conversation[0]] + conversation[-MAX_HISTORY:]

    response = ollama.chat(
        model="llama3",
        messages=conversation
    )

    bot_reply = response["message"]["content"]

    print("Chatbot:", bot_reply)

    conversation.append({"role": "assistant", "content": bot_reply})