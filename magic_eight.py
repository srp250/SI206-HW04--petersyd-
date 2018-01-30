import random
from random import randrange




answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely"
"You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes"
"Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now"
"Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no"
"My sources say no", "Outlook not so good", "Very doubtful"]


def user_prompt():
    responses = []
    user_response = input("What is your question?")
    responses.append(user_response)


    print(responses)

def random_choice():
    print(random.choice(answers))


user_prompt()
random_choice()
