import random

print("Welcome to the Word guess game!!")

words=['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("Guess the characters")
turns = 12
guesses= ' '

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end="")
        else :
            print("_ ", end="")
            failed+= 1
        
    if failed ==0:
            print("\nYou Win")
            print("The word is", word)
            break

    print()
    
    guess = input("guess a character ")
    guesses+= guess

    if guess not in word:
        turns-=1
        print("Wrong")
        print("You have",+ turns," chances!! More guesses")

        if turns == 0:
            print("You lost!!")



