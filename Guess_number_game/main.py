import random

# step_1 Generate random number
SECRET_NUMBER = random.randint(0, 100)

EASY = 10
HARD = 5
# step_2 Select level
select_level = input("chose difficulty type 'easy' or 'hard' : ")

if select_level == "easy":
    chances = EASY
else:
    chances = HARD

is_playing = True
while is_playing:
    chances = chances -1
    if chances >=0:
        user_guess = int(input("Guess the number:"))
        if user_guess > SECRET_NUMBER:
            print("It's too high.")
        elif user_guess < SECRET_NUMBER:
            print("It's too low.")
        elif user_guess == SECRET_NUMBER:
            print("you win!!!!")
            break
    else:
        is_playing = False
        print("you loose!!!")
