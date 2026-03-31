import ollama

print("🤖 Chatbot with memory started! Type 'exit' to quit.\n")

conversation = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    # Add user message
    conversation.append({"role": "user", "content": user_input})

    response = ollama.chat(
        model="llama3",
        messages=conversation
    )

    bot_reply = response["message"]["content"]

    print("Chatbot:", bot_reply)

    # Add bot response to memory
    conversation.append({"role": "assistant", "content": bot_reply})