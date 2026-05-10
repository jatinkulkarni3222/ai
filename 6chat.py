import random
from nltk.chat.util import Chat, reflections

# Context memory
context = {
    "last_topic": None
}

pairs = [

    # Greetings
    [
        r"hi|hello|hey|hii|good morning|good evening",
        ["Hello! Welcome to ABC Bank. How can I assist you today?"]
    ],

    # Name
    [
        r"my name is (.*)",
        ["Hello %1, nice to meet you! How can I help you today?"]
    ],

    # Balance
    [
        r"(.*)balance(.*)",
        ["You can check your balance using our mobile app or website."]
    ],

    # Loan general
    [
        r"(.*)loan(.*)",
        ["We offer home, personal, and car loans. Which one are you interested in?"]
    ],

    # Loan types (IMPORTANT: placed above fallback)
    [
        r"(home loan|personal loan|car loan)",
        ["Great choice! %1 is available. Would you like to know eligibility or interest rates?"]
    ],

    # Loan details follow-up
    [
        r"(eligibility|criteria|interest|rate)",
        ["Loan eligibility depends on income, credit score, and employment status."]
    ],

    # Card issues
    [
        r"(.*)(lost|stolen|block)(.*)card(.*)",
        ["Please immediately call 1800-123-456 to block your card."]
    ],

    # Open account
    [
        r"(.*)open(.*)account(.*)",
        ["You can open an account online or visit your nearest branch with valid ID proof."]
    ],

    # Working hours
    [
        r"(.*)(working hours|timing|open time)(.*)",
        ["Our bank operates from 9 AM to 5 PM, Monday to Friday."]
    ],

    # Branch
    [
        r"(.*)(branch|location|near me)(.*)",
        ["You can find your nearest branch using Google Maps or our website."]
    ],

    # Thanks
    [
        r"thanks|thank you",
        ["You're welcome!", "Happy to help!"]
    ],

    # Exit
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day."]
    ],

    # Fallback
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Could you rephrase?"]
    ]
]

chatbot = Chat(pairs, reflections)


def start_chat():
    print("===================================")
    print(" Welcome to ABC Bank Chatbot 🤖")
    print(" Type 'bye' to exit")
    print("===================================")

    while True:
        user_input = input("You: ").lower().strip()

        # Exit manually handled
        if user_input in ["bye", "exit", "quit"]:
            print("Bot:", random.choice([
                "Goodbye! Have a great day.",
                "Thank you for visiting ABC Bank!"
            ]))
            break

        # Context tracking (simple)
        if "loan" in user_input:
            context["last_topic"] = "loan"

        elif user_input in ["home loan", "personal loan", "car loan"]:
            context["last_topic"] = "loan_type"

        # Generate response
        response = chatbot.respond(user_input)

        # Context-aware enhancement
        if context["last_topic"] == "loan" and user_input in ["home loan", "personal loan", "car loan"]:
            response = f"Great choice! {user_input.title()} is available. Do you want eligibility details?"

        print("Bot:", response)


if __name__ == "__main__":
    start_chat()
# python3 -m venv venv
# source venv/bin/activate
# pip install nltk
# python3 Assignment5.py

# You: hi
# Bot: Hello! Welcome to ABC Bank. How can I assist you today?
# You: my name is Vinayak 
# Bot: Hello vinayak, nice to meet you! How can I help you today?
# You: I want a loan
# Bot: We offer home, personal, and car loans. Which one are you interested in?
# You: home loan
# Bot: Great choice! Home Loan is available. Do you want eligibility details?
# You: what is eligibility
# Bot: I'm sorry, I didn't understand that. Could you rephrase?
# You: I lost my card
# Bot: Please immediately call 1800-123-456 to block your card.
# You: bye
# Bot: Thank you for visiting ABC Bank!