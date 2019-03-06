from random import randint
#Initializing the variable to be the score for the players
player_wins = 0
computer_wins = 0
#When the scoring will stop when we reached a certain number
winning_score = 3

#starting the loop of while
while player_wins < winning_score and computer_wins < winning_score:
    #printing out first the score
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")

    player = input("(Enter your choice): ").lower()
    ## If a player wants to quit the game
    if player == "quit" or player == "q":
        break
    random_num = randint(0, 2)
    if (random_num == 0):
        computer = "rock"
    elif (random_num == 1):
        computer = "paper"
    else:
        computer = "scissors"

    print(f"The computer plays: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer wins :( ")
            #adding 1 to the initialized variable at the top
            computer_wins += 1
        else:
            print("Player wins!")
            player_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif (player == "scissors"):
        if (computer == "rock"):
            print("Computer wins!")
            computer_wins += 1
        else:
            print("You win!")
            player_wins += 1
    else:
        print("Please enter a valid move!")

if player_wins > computer_wins:
    print(f"CONGRATS, YOU WON!, final score player = {player_wins} and computer = {computer_wins}")
elif player_wins == computer_wins:
    print(f"ITS A TIE!, final score player = {player_wins} and computer = {computer_wins}")
else:
    print(f"OH NO :( THE COMPUTER WON..., final score computer = {computer_wins} and player = {player_wins}")

