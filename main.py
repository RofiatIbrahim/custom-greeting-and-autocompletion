import random
user_input = input().title()
dictionary = ["Bank Transfer", "Pay Bills", "Airtime Purchase", "Send Airtime", "Data Purchase", "Transfer Money"]
greetings = ["Hello", "Hi", "Namaste", "Howdy", "Hey", "Good day", "How do you do", "Greetings"] 
if user_input in greetings:
    response = random.choice(greetings)
    print(response)
else:
    for word in dictionary:
        if word.title().startswith(user_input):
            print(word)
            break
    else:
        print("Not Available")
