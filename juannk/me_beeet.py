import random


def rps():
    rps1 = ["r", "p", "s"]
    computer_choice = random.choice(rps1)
    player_choice = input("please enter 'r', 'p', 's':\n")
    while player_choice == 'r' or player_choice == 'p' or player_choice == 's':
        try:
            print(f"computer choose {computer_choice} and you choose {player_choice}")
            break
        except:
            player_choice = input("Error! please input either r, p, or s")
    if player_choice == computer_choice:
        print("it is a tie")
    elif player_choice == "r" and computer_choice == "s":
        print("yee you won!!!")
    elif player_choice == "s" and computer_choice == "p":
        print("you won woo_hoo!!!")
    elif player_choice == "p" and computer_choice == "r":
        print("ye you won!!!")
    else:
        print("you lose boo_hoo!!!")


rps()
