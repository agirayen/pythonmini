import random

player1 = input("Select one of the following Rock,Paper,Scissor :  ").lower()

player2 = random.choice(["Rock","Paper","Scissor"]).lower()

print("Player2 selected : ",player2)

if player1 == "Rock" and player2 == "paper":
    print("paper covered rock and player2 won")

elif player1 == "paper" and player2 == "Scissor":
    print("player2 won")

elif player1 == "Scissor" and player2 == "Rock":
    print("player2 won")

elif player1 == player2:
    print("tie")

else:

    print("Player1 won")
    
