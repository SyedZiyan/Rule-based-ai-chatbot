print("=" * 40)
print("🤖 Rule-Based AI Chatbot")
print("Type 'bye' or 'exit' to quit")
print("=" * 40)

while True:
    user = input("\nYou: ").lower()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif user == "how are you":
        print("Bot: I am doing well. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is RuleBot.")

    elif user == "who created you":
        print("Bot: I was created as a Rule-Based AI Chatbot project.")

    elif user in ["bye", "exit"]:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that command.")
