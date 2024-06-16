import re
def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you?")
    while True:
        user_input = input("You: ").strip().lower()
        if re.search('\\b(hi|hello|hey)\\b', user_input):
            print("Chatbot: Hello! How can I help you?")
        elif re.search('\\b(how are you|how are you doing)\\b', user_input):
            print("Chatbot:I'm doing well, what about you?")
        elif re.search('\\b(what is your name|who are you)\\b', user_input):
            print("Chatbot: I'm a simple chatbot made by Ola Saleh.")
        elif re.search('\\bweather\\b', user_input):
            print("Chatbot: I'm not connected to the internet, but you can check it on any weather website.")
        elif re.search('\\b(day|date)\\b', user_input):
            print("Chatbot: I'm not sure what the date is, but you can check it on your phone calendar.")
        elif re.search('\\btime\\b', user_input):
            print("Chatbot: I can't tell the time, but you can check it on your phone.")
        elif re.search('\\b(bye|goodbye|exit)\\b', user_input):
            print("Chatbot: Goodbye! Have a nice day!")
            return
        elif re.search('\\b(thank you|thanks)\\b', user_input):
            print("Chatbot: You're welcome! How else can I help you?")
        elif re.search('\\b(help|assist)\\b', user_input):
            print("Chatbot: Sure, just tell me... What do you need help with?")
        elif re.search('\\bwho created you\\b', user_input):
            print("Chatbot: I was created by Ola Saleh using Python.")
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")
chatbot()