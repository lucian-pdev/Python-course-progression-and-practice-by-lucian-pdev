# cython: language_level=3

import random

# Define a list of words to choose from.
cdef list word_list = ["aardvark", "baboon", "camel"]

# Declare lives as an integer.
cdef int lives = 6

print(f"Hangman game, let's go, you have {lives} lives!")

# Randomly select a word.
cdef str chosen_word = word_list[random.randint(0, len(word_list) - 1)]
print(f"Test print, chosen word : {chosen_word}.")  # TESTING_PRINT

# ASCII art stages.
cdef list HANGMAN_PICS = [
    r'''
  +---+
  |   |
      |
      |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]
HANGMAN_PICS.reverse()


def user_guess():
    while True:
        guess = input("Type a letter: ")
        if guess.isalpha():
            guess = guess.lower()
            break
        else:
            print("A letter, no numbers, symbols or spaces, please.")
    return guess


def guess_correct(guess: str, chosen_word: str, lives: int) -> int:
    if guess in chosen_word:
        print("Right")
    else:
        print("Wrong")
        lives -= 1
        if lives > 0:
            print(f"{lives} left...")
    return lives


# Create a placeholder hint string.
cdef str placeholder = ""
cdef int i
for i in range(len(chosen_word)):
    placeholder += "_"
print("Hint:")
print(placeholder)

# Create a hidden-check list to track found letters.
cdef list hidden_check = []
for i in range(len(chosen_word)):
    hidden_check.append(False)


def display_progress(hidden_check, guess: str, chosen_word: str) -> str:
    cdef str display = ""
    cdef int position
    for position in range(len(hidden_check)):
        if not hidden_check[position]:
            # Since chosen_word[position] is a single letter,
            # compare it directly with guess.
            if guess == chosen_word[position]:
                display += chosen_word[position]
                hidden_check[position] = True
            else:
                display += "_"
        else:
            display += chosen_word[position]
    return display


def main():
    global lives, chosen_word, hidden_check
    while False in hidden_check and lives > 0:
        guess = user_guess()
        lives = guess_correct(guess, chosen_word, lives)
        if lives == 0:
            break
        display_str = display_progress(hidden_check, guess, chosen_word)
        print(display_str)

    if lives > 0:
        print("You win!")
    else:
        print("You loose!")


if __name__ == '__main__':
    main()
