import random # It is used for suggest any random number

def guessing_game():
    # Welcome Message
    print("Hello User! Let's play the guessing game.")
    print("Let's see how fast you can read my mind!!!")
    print("-"*45)
    # Computer guesses a random number between user input interval
    print("In which interval are you preffered to guess a number ??")
    start = int(input("Enter the starting number:"))
    end = int(input("Enter the ending number:"))
    print("-"*45)
    print(f"As per your preference the computer choose a random number between {start} and {end}")
    print("!!! Now it's your turn to guess the number !!!")
    GuessNum_Computer = random.randint(start, end)
    GuessNum_User = None
    Num_try = 0

    while(GuessNum_Computer != GuessNum_User):
        try:
            GuessNum_User = int(input(f"Guess a number between {start} and {end}: "))
            if (GuessNum_User < start or GuessNum_User > end):
                print(f"Please enter a number within the range {start} to {end}.")
                print("-"*30)
                continue
        except ValueError as ve:
            print(ve)
            #print("Invalid input. Please enter an integer.")
            print("-"*30)
            continue

        if GuessNum_Computer == GuessNum_User:
            print("You guessed the right number!!!")
        elif GuessNum_Computer > GuessNum_User:
            print(f"You guessed the wrong number. Try a higher number between {GuessNum_User} and {end}.")
            start = GuessNum_User + 1
        else:
            print(f"You guessed the wrong number. Try a lower number between {start} and {GuessNum_User}.")
            end = GuessNum_User - 1
        print("-"*30)
        Num_try += 1 #This iterator count how many time user guess the number

    print('\n')
    print(f"You guessed the right number {GuessNum_Computer} in {Num_try} tries.")

#Call the function
guessing_game()
