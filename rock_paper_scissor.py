import random  # this a library and it randomly choose our datas


def get_choices():  # this is a function
    while True:  # this is a do while loops & it is making sure that we input the right value
        player_choice = input("enter a choice(rock,paper,scissor): ").lower()
        if player_choice in ["rock", "paper", "scissor"]:
            break
        else:
            print("Error:please enter only(rock,paper or scissors.")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer): # this is also a function that is checking on who won the game
    print(f"you chose: {player}, computer chose: {computer} ")
    if player == computer:
        return "it's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "rock smashes scissors! you win"
        else:
            return "you lose wahahaha cry baby"
    elif player == "paper":
        if computer == "rock":
            return "paper eats rock ! you win"
        else:
            return "you lose wahahaha cry baby"
    elif player == "scissors":
        if computer == "paper":
            return "scissors tears paper! you win"
        else:
            return "you lose wahahaha cry baby"


choices = get_choices() # over here we are calling the fuction above
result = check_win(choices["player"], choices["computer"])
print(result)