import random
from wsgiref.util import guess_scheme

words = ['python', 'java', 'flask', 'django', 'javascript', 'cpp', 'swift', 'ruby']

chosen_word = random.choice(words)  # Randomly choose a word from the list
word_display = ['_' for i in chosen_word]
attempts = 5    # Giving 5 attempts to user

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + " ".join(word_display))
    guess = input("Enter a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("That letter doesn't appear in the word")
        attempts -= 1
        if attempts > 0:
            print(f"You have more {attempts} attempts to guess the word")
        else:
            print("You ran out of attempts")

if '_' not in word_display:
    print("You guessed the word!")
    print(" ".join(word_display))
    print("You survived!")
else:
    print(f"The word was '{chosen_word}'")
    print("You lost")
