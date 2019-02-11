###randomizing th einput of 1 player
### translate a random number to put it on a random pick


import random
'''print("Rock")
print("Paper")
print("Scissor")
'''

player = input("Make your move : ")
computerpick = random.randint(0,2)
if computerpick == 0:
    computer = "rock"
elif computerpick == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"computer plays {computer}")


if player == "" and computer == "":
    print("input something")
elif player == computer:
    print("its a tie")
elif player == "rock":
    if computer == "scissors":
        print("player wins")
    elif computer == "paper":
        print("computer wins")
elif player == "paper":
    if computer == "rock":
        print("player wins")
    elif computer == "scissors":
        print("computer wins")
elif player == "scissors":
    if computer == "rock":
        print("computer wins")
    elif computer == "paper":
        print("player wins")

else:
    print("something went wrong")