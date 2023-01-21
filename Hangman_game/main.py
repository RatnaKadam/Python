import random
from hangman_art import stages, logo
from hangman_words import word_list

# Chose a word randomly
chosen_word = random.choice(word_list)
print(chosen_word)

blank_spaces = []

for item in range(len(chosen_word)):
    blank_spaces.append("_")

print(blank_spaces)

lives_remaining = 6
guessing_continue = True
img_count = 6
print(logo)

# run the loop until you guess the word or looses all lives
while guessing_continue:
    guess = input("Guess the letter: ").lower()
    print(stages[img_count])

    # check input in chosen word
    for position in range(len(chosen_word)):
        char = chosen_word[position]
        if char == guess:
            blank_spaces[position] = guess
    print(blank_spaces)

    # loose condition
    if guess not in chosen_word:
        lives_remaining = lives_remaining - 1
        img_count = img_count - 1
        if lives_remaining == 0:
            print("You loose!!!")
            guessing_continue = False
    print(stages[img_count])

    # win condition
    if "_" not in blank_spaces:
        print("You win!!!")
        guessing_continue = False
