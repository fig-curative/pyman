import sys
import random

def main():
    def get_word():
        with open("wordlist.txt") as file:
            all_file = file.read()
            possible_words = all_file.split()
            secret_word = random.choice(possible_words)
            secret_word = secret_word.upper()
        return secret_word
    
    secret_word = get_word()
    print(f"{secret_word}") # for testing, remove later
    guessed_letters = []
    guess_display = ["_"] * len(secret_word)
    
    strikes = 0

    print("Welcome to pyman, a simple hangman game in Python. Try to guess the word. If you guess three incorrect letters, you lose!")
    print("Guess the word!:")
    print("\n" + " ".join(guess_display))

    while True:
        # did player win?
        if "".join(guess_display) == secret_word:
            print("That's right! The word was:")
            print(f"{secret_word}")
            print("You won!")
            sys.exit()
        
        # player hasn't won yet:
        player_guess = input("Please guess a letter: ")
        player_guess = player_guess.upper()

        if not player_guess.isalpha() or len(player_guess) > 1:
            print("Guess must be a single letter.")
        else:
            if player_guess in guessed_letters:
                print(f"You already guessed {player_guess}. Pick a different letter.")
                print("\n" + "You have guessed:")
                print(" ".join(guessed_letters))
            elif player_guess in secret_word:
                guessed_letters.append(player_guess)
                print("\n" + f"Good guess! {player_guess} is in the word.")

                for index, letter in enumerate(secret_word):
                    if letter == player_guess:
                        guess_display[index] = player_guess

            elif player_guess not in secret_word:
                guessed_letters.append(player_guess)
                strikes += 1
                if strikes == 1:
                    print(f"{player_guess} is not in the word.")
                    print(" O")
                elif strikes == 2:
                    print(f"{player_guess} is not in the word.")
                    print(" O")
                    print("/|\\")
                elif strikes >= 3:
                    print(f"{player_guess} is not in the word.")
                    print(" O")
                    print("/|\\")
                    print(" /\\")
                    print("You've been hanged. Game over!")
                    sys.exit()

        print("\n" + " ".join(guess_display))

if __name__ == "__main__":
    main()
