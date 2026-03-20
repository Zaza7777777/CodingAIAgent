from chat import chat

print("Type 'quit' to exit")
while True:
    user_input = input("\nUser: ").strip()
    if user_input.lower() == "quit":
        break
    if user_input:
        print(f"Assistant: {chat(user_input)}")
        