# Define a function to handle user input and generate responses
def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input == 'hi' or user_input == 'hello':
        return "Hello! How can I assist you today?"
    elif user_input == 'how are you?' or user_input == 'how are you doing?':
        return "I'm just a computer program, so I don't have feelings, but I'm here to help you!"
    elif user_input == 'what is your name?' or user_input == 'who are you?':
        return "I'm a simple chatbot. You can call me ChatBot."
    elif user_input == 'quit':
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase or ask something else?"

# Main function to handle the conversation loop
def main():
    print("Welcome to ChatBot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("ChatBot:", response)
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    main()
