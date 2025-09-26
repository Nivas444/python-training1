print("Hello! I'm your chatbot. Type 'bye' to end the chat.\n")

while True:
    user_input = input("You: ").lower()
    if user_input == "hi" or user_input == "hello":
        print("Chatbot: Hello there! How are you?")
    elif "im fine" in user_input:
        print("Chatbot: I'm too fine, thank you! How can I assist you today?")
    elif "what is your name" in user_input:
        print("Chatbot: I'm a simple Python chatbot.")
    elif "bye" in user_input:
        print("Chatbot: Goodbye! Have a nice day")
        break
    else:
        print("Chatbot: Sorry, I don't understand that.")
