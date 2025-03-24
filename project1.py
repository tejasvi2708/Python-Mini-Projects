import random

print("Hi Welcome to the Number Guessing Game!!\nYou got 7 chances to guess the number. Let's start the game")

number_to_guess =random.randrange(100)

chances = 7

guess_counter = 0

while guess_counter < chances:

    guess_counter+=1
    user_guess = int(input("Guess the number "))

    if number_to_guess == user_guess:
        print(f' Congratulations! You guess the number {number_to_guess} in {guess_counter} chance.')
        break

    elif guess_counter >= chances and user_guess!=number_to_guess:
        print(f"Oops Sorry!! The number is {number_to_guess}\nBetter Luck next time")

    elif user_guess > number_to_guess:
        print("You guessed high")

    elif user_guess < number_to_guess:
        print("You guessed low")
