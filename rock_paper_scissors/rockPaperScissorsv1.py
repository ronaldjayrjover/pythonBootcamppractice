print("Rock")
print("Paper")
print("Scissor")

player1 = input("Make your move P1: ")
player2 = input("Make your move P2: ")

if player1 == "rock" and player2 == "scissors":
    print("player 1 wins")
elif player1 == "rock" and player2 == "paper":
    print("player2 wins")

elif player1 == "paper" and player2 == "rock":
    print("player1 wins")
elif player1 == "paper" and player2 == "scissors":
    print("player2 wins")

elif player1 == "scissors" and player2 == "paper":
    print("player1 wins")
elif player1 == "scissors" and player2 == "rock":
    print("player2 wins")

if player1 == "" and player2 == "":
        print("input something")
elif player1 == player2:
        print("its a tie")
else:
    print("something went wrong")