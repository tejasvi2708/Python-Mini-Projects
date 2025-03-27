import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:

    print("Enter your choice \n 1: Rock\n 2: Paper\n 3: Scissiors\n")

    # Input from User
    choice = int(input("Enter your Choice "))
     
     # Looping until user enters valid input
    while choice > 3 or choice < 1:
        choice=int(input("Please enter valid choice! "))

    # Initialize value of choice_name variable corresponding to the choice value
    if choice == 1:
        user_choice = 'Rock'
    elif choice ==2:
        user_choice = 'Paper'
    else:
        user_choice = 'Scissiors'
    
    print("User's choice is ",user_choice)
    print("Now its Computer's Turn -")

    comp_choice = random.randint(1,3)

     # Initialize value of comp_choice_name variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice ==2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissiors'
      
    print("Computer's choice is ", comp_choice_name)

    print(user_choice,"vs",comp_choice_name)

    # Determine the winner
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (choice ==2 and comp_choice == 1):
        result = 'Paper'
    elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
        result = 'Scissiors'
    elif (choice == 3 and comp_choice == 1) or (choice == 1 and comp_choice == 3):
        result = 'Rock'

    if result =="DRAW":
        print("It's a tie")
    elif result == user_choice:
        print("USER WINS!!")
    else:
        print("COMPUTER WINS!!")

    print("Do you want to play again (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

print("Thanks for playing!!")
    

        