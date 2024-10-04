import re
import random

class JoerAI:
    def __init__(self):
        self.patterns = [
            (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
            (r'how are you', ['I'm doing well, thanks!', 'I'm great, how about you?']),
            (r'what is your name', ['My name is JoerAI.', 'I'm JoerAI, nice to meet you!']),
            (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
            (r'(\w+) your favorite (color|food|movie)', ['As an AI, I don\'t have preferences, but I find {1}s interesting!']),
            (r'tell me a joke', ['Why don\'t scientists trust atoms? Because they make up everything!', 
                                 'What do you call a fake noodle? An impasta!']),
        ]

    def respond(self, user_input):
        user_input = user_input.lower()
        for pattern, responses in self.patterns:
            match = re.search(pattern, user_input)
            if match:
                response = random.choice(responses)
                return response.format(*match.groups())
        return "I'm not sure how to respond to that. try rephrasing that, or try something else"

def main():
    joer = JoerAI()
    print("JoerAI: Hello! I'm JoerAI. ")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("JoerAI: Goodbye! Have a great day!")
            break
        response = joer.respond(user_input)
        print("JoerAI:", response)

if __name__ == "__main__":
    main()
