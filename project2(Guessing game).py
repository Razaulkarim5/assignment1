import random
import itertools  # to create an infinite loop for attempts

def num_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the  integer number between 1 and 100.")
    #  Random Number Generation
    secret_number = random.randint(1, 100)
    # for loop with no limit on attempts
    for attempts in itertools.count(1):  # Infinite loop, starting at 1 for attempts
        try:
            #  Handle user input
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("The number is out of range! Please enter a number between 1 and 100.")
                continue
            #  Conditional logic for feedback
            if guess < secret_number:
                print("Too low! \n")
            elif guess > secret_number:
                print("Too high!\n")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 100.")
# Call function to run the game
num_guessing_game()
