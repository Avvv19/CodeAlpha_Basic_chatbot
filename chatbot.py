import nltk
import random
from nltk.chat.util import Chat, reflections
from datetime import datetime

# Define some conversation patterns
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I\'m doing well, thank you!', 'I\'m good, thanks for asking.']),
    (r'today date', [f'Today\'s date is {datetime.now().strftime("%Y-%m-%d")}.']),
    (r'what\'s your name?', ['My name is ChatBot.']),
    (r'what can you do?', ['I can have basic conversations with you.']),
    (r'quit|exit', ['Thank you! Have a nice day.']),
]

# Create a chatbot using the defined patterns
chatbot = Chat(patterns, reflections)

def chat():
    print("Welcome to the chatbot!")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("ChatBot:", response)
        if user_input.lower() in ['quit', 'exit']:
            break

if __name__ == "__main__":
    chat()
