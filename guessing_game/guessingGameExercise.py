'''
Computer will pick between 1 and 10
Do you want to keep playing? (Y/N)
'''

import random

random_number = random.randint(1, 10)
guess = None

while guess != random_number:
    guess = int(input("guess the number: "))
    #guess_again = input("")
    if random_number > guess:
        print("guess high\n")
    elif random_number < guess:
        print("guess low\n")
    else:
        print("You guessed it\n")
        # print("Do you want to keep playing? Y/N")
        #     if guess_again == "Y":
        #         random_number = random.randint(1, 10)
        #         print(guess)
        #     else:
        #         guess_again == "N"
        #         break








