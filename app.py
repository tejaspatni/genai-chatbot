import ollama

response = ollama.chat(
    model="llama3",
    messages=[
        {"role": "user", "content": "Explain what a transformer is in simple terms."}
    ]
)

print(response["message"]["content"])