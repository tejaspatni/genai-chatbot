import ollama

print("🤖 Smart Chatbot started! Type 'exit' to quit.\n")

# System prompt (VERY IMPORTANT)
conversation = [
    {
        "role": "system",
        "content": "You are a helpful AI tutor who explains concepts in simple and clear terms. Always give structured answers."
    }
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    conversation.append({"role": "user", "content": user_input})

    response = ollama.chat(
        model="llama3",
        messages=conversation
    )

    bot_reply = response["message"]["content"]

    print("Chatbot:", bot_reply)

    conversation.append({"role": "assistant", "content": bot_reply})