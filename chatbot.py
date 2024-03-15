import random

# Dictionary containing responses for different user inputs
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    "what's your name": ["I'm a chatbot!", "You can call me ChatBot."],
    "what do you do": ["I'm here to chat with you!", "I'm a conversational agent."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!",
                       "I'm not good at jokes, but here's one: Why was the math book sad? Because it had too many problems."],
    "who created you": ["I was created by a team of developers.", "My creators prefer to remain anonymous."],
    "what is the weather today": ["I'm sorry, I can't provide real-time information.",
                                  "You can check the weather on a weather website or app."],
    "how old are you": ["I don't have an age. I'm just a program!", "I exist in the realm of ones and zeros, so I don't age."],
    "what is the meaning of life": ["The meaning of life is a philosophical question that has puzzled humans for centuries.",
                                    "I think the meaning of life is subjective and varies from person to person."]
}

# Function to get response from the bot
def get_response(user_input):
    if user_input.lower() in responses:
        return random.choice(responses[user_input.lower()])
    else:
        return "I'm sorry, I don't understand that."

# Main function to run the chatbot
def main():
    print("Welcome to the ChatBot!")
    print("You can start chatting. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(get_response(user_input))
            break
        else:
            print("ChatBot:", get_response(user_input))

if __name__ == "__main__":
    main()
