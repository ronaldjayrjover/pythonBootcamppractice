'''
Computer will pick between 1 and 10
Do you want to keep playing? (Y/N)
'''

import random

random_number = random.randint(1, 10)

while True:
    guess = int(input("guess the number: "))
    if random_number > guess:
        print("guess high\n")
    elif random_number < guess:
        print("guess low\n")
    else:
        print("You guessed it\n")
        play_again = input("Do you want to keep playing? Y/N")
        if play_again == "Y":
            random_number = random.randint(1, 10)
            guess = None
        else:
            print("Thank you")
            break








