import random
roll = ["rock" , "paper", "scissors"]
computer_choice = random.choice(roll)



def get_choice():
    player_choice = input("Enter a choice rock, paper, scissors: ") 
    roll = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(roll)
    Choices= {"Player" : player_choice, "computer" : computer_choice}
    return Choices

def check_win(player, computer):
   # print("You chose " + player + " , computer chose" + computer)
    if player == computer:
        return "It's a tie"
    
Choices = get_choice()
player_roll = Choices["Player"]
print(f"Your choice is {player_roll}")

computer_roll = Choices["computer"]
print(f"The computer choice is {computer_roll}")

#Player_Roll = Choices["Player"]
##print(Choices)


