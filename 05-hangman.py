from random import choice
from string import ascii_uppercase
from wordlist import words

def get_valid_word(words):
    word = choice(words) # randomly chooses a word from the list

    while "-" in word or " " in word:
        word = choice(words)

    return word.upper()

def check_winner(lives, word):
    if lives == 0:
        print(f"You did, sorry. The word was {word}")

    else:
        print(f"Yay! You guessed the word '{word}'!")

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} attempts left and you have used these letters: {' '.join(used_letters)}")

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(f"Current word: {' '.join(word_list)}")

        user_chosen_letter = input("Guess a letter: ").upper()

        if user_chosen_letter in alphabet - used_letters:
            used_letters.add(user_chosen_letter)

            if user_chosen_letter in word_letters:
                word_letters.remove(user_chosen_letter)
                print("")
            
            else:
                lives -= 1
                print(f"\nYour letter '{user_chosen_letter}' is not in the word.")

        elif user_chosen_letter in used_letters:
            print("\nYou have already used that letter. Guess another letter.")

        else:
            print("\nThat is not a valid letter.")

    check_winner(lives, word)

if __name__ == "__main__":
    hangman()
