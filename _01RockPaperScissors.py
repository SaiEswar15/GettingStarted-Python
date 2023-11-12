# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

import random

def game():
    player_choice = input("Enter your chioce : Rock, Paper, Scissors : ")
    
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    return validate_game(player_choice, computer_choice)
    
    
def validate_game(player_choice, computer_choice) :
    if(player_choice == computer_choice) :
        print(f"Player chose {player_choice} and computer chose {computer_choice} ")
        return "Its a tie...."
        
    else :
        if(player_choice == "Rock"):
            print(f"Player chose {player_choice} and computer chose {computer_choice} ")
            if(computer_choice == "Paper"):
                return "Paper covers Rock. So you win:)"
            else :
                return "Rock destroys Scissors. So you lose:("
        elif(player_choice == "Paper"):
            print(f"Player chose {player_choice} and computer chose {computer_choice} ")
            if(computer_choice == "Rock"):
                return "Paper covers Rock. So you win:)"
            else :
                return "Scissors cut Paper. So you lose:("
        else :
            print(f"Player chose {player_choice} and computer chose {computer_choice} ")
            if(computer_choice == "Rock"):
                return "Rock destroys Scissors. So you lose:("
            else :
                return "Scissors cut Paper. So you lose:("
            
print(game())
    