###refactor of V1

print("Rock")
print("Paper")
print("Scissor")

player1 = input("Make your move P1: ")
player2 = input("Make your move P2: ")


if player1 == "" and player2 == "":
    print("input something")
elif player1 == player2:
    print("its a tie")
elif player1 == "rock":
    if player2 == "scissors":
        print("player1 wins")
    elif player2 == "paper":
        print("player2 wins")
elif player1 == "paper":
    if player2 == "rock":
        print("player1 wins")
    elif player2 == "scissors":
        print("player2 wins")
elif player1 == "scissors":
    if player2 == "rock":
        print("player2 wins")
    elif player2 == "paper":
        print("player1 wins")

else:
    print("something went wrong")