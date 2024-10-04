import re

def simple_chatbot(user_input):
    # Convert input to lowercase for easier matching
    user_input = user_input.lower()

    # Define some simple patterns and responses
    patterns = {
        r'hi|hello|hey': 'Hello! How can I help you today?',
        r'how are you': "I'm doing well, thank you for asking. How about you?",
        r'what is your name': "My name is SimpleBot. It's nice to meet you!",
        r'bye|goodbye': 'Goodbye! Have a great day!',
        r'thank you|thanks': "You're welcome! Is there anything else I can help with?",
        r'weather': "I'm sorry, I don't have access to real-time weather information.",
        r'help': "I'm a simple chatbot. You can ask me basic questions or just chat with me!",
    }

    # Check input against patterns and return appropriate response
    for pattern, response in patterns.items():
        if re.search(pattern, user_input):
            return response

    # Default response if no pattern matches
    return "I'm not sure how to respond to that. Can you try rephrasing or asking something else?"

def main():
    print("SimpleBot: Hello! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("SimpleBot: Goodbye! Have a great day!")
            break
        
        response = simple_chatbot(user_input)
        print("SimpleBot:", response)

if __name__ == "__main__":
    main()

