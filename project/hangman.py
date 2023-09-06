import random
from words2 import words
import string


def get_valid_word(words):
    word = random.choice(words["data"])  # randomly choose something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    numb_games = 0
    games_played = 0
    while games_played <= 0:
        try:
            games_played = int(input("how many games do you want to play: "))
        except:
            print("you must enter a number.")

    while numb_games < games_played:
        games_played -= 1
        print("*" * 30)
        print(f"Game {numb_games} of {games_played}")
        print("*" * 30)
        word = get_valid_word(words)
        word_letters = set(word)  # letters in the word
        alphabet = set(string.ascii_uppercase)
        used_letters = set()  # what the user has guessed

        lives = 6

        # getting user input
        while len(word_letters) > 0 and lives > 0:
            # letters used
            print("you have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

            # what current word is (ie w-rd)
            word_list =[letter if letter in used_letters else "-" for letter in word]
            print("current word: ", " ".join(word_list))
            user_letter = input("Guess a letter: ").upper()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)

                else:
                    lives -= 1
                    print("letter not in the word.")

            elif user_letter in used_letters:
                print("you have already used that character, please try again.")

            else:
                print("invalid character")

        # gets here when len(word_letters) == 0
        if lives == 0:
            print("you died, sorry the word was: ", word)
        else:
            print("you have guessed the word: ", word)
    print("\nThank you for playing.")


if __name__ == "__main__":
    get_valid_word(words)
    hangman()
