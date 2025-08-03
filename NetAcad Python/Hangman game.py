# HANGMAN GAME
import random

word_list = ["aardvark", "baboon", "camel"]

lives = 6

print(f"Hangman game, let's go, you have {lives} lives!")

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
print(f"Test print, chosen word : {chosen_word}.")  # TESTING_PRINT

# ASCII art stages:
HANGMAN_PICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
HANGMAN_PICS.reverse()


# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.


def user_guess():
    while True:
        guess = input("Type a letter.")
        if guess.isalpha():
            guess = guess.lower()
            break
        else:
            print(f"A letter, no numbers, symbols or spaces, please.")
            continue
    return guess


# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
def guess_correct(guess, chosen_word, lives):
    if guess in chosen_word:
        print("Right")
    else:
        print("Wrong")
        lives -= 1
        if lives > 0:
            print(f"{lives} left...")
    return lives


# TODO-4 - Create placeholder variable and hint
placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(f"""Hint: 
{placeholder}""")

# Personal initiative: hidden list to keep track of correct letters
hidden_check = []
for letter in chosen_word:
    hidden_check.append(False)


# TODO-5 - Display progress
def display_progress(hidden_check, guess, chosen_word):
    display = ""
    for position in range(len(hidden_check)):
        if not hidden_check[position]:
            if guess in chosen_word[position]:
                display += chosen_word[position]
                hidden_check[position] = True
            else:
                display += "_"
        else:
            display += chosen_word[position]
    return display


# TODO-6 - loop the guess to game finish
while False in hidden_check and lives > 0:
    guess = user_guess()
    lives = guess_correct(guess, chosen_word, lives)  # TODO-8 - Check lives
    if lives == 0:
        break
    display = display_progress(hidden_check, guess, chosen_word)
    print(f"{display}")

# TODO-7 - win declaration
if lives > 0:
    print("You win!")
else:
    print("You loose!")
