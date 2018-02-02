import random

def user_prompt():
    user_response = input("What is your question?")

    answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely"
    "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes"
    "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now"
    "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no"
    "My sources say no", "Outlook not so good", "Very doubtful"]

    if user_response[-1] != '?':
        print('I am sorry, I can only answer questions.')

    while user_response != "quit":
        if user_response[-1] != '?':
            print('I am sorry, I can only answer questions.')

        else:
            print(random.choice(answers))

        if user_response == "quit":
            print("See you next time")

        user_response = input("What is your question?")

user_prompt()
