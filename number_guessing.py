# 3. Number Guessing Game
# Objective: Build a guessing game where the user guesses a randomly generated number.
# Steps:
# 1. Use Python’s random module to generate a number between 1 and 100.
# 2. Allow the user to guess the number.
# 3. Provide feedback ("Too high" or "Too low").
# 4. Limit the number of attempts to 5.
# 5. Display a success or failure message at the end.

import random

def number_guessing():
    random_number = random.randint(1, 100)
    tries = 5
    while tries > 0:
        try:
            user_input = int(input("Enter a number between 1 and 100: "))
            if user_input == random_number:
                print("Congratulations! You guessed the correct number.")
                break
            else:
                tries-=1
                if user_input < random_number-10:
                    print("Too low. Try again.\n")
                elif user_input > random_number+10:
                    print("Too high. Try again.\n")
                else:
                    print("Close, but not correct. Try again.\n")
                print(f"You have {tries} tries left.\n")    
        except ValueError:
            print("Please try again :")
    if tries == 0:
        print(f"Sorry, you have run out of tries. The correct number was {random_number}.") 
        
number_guessing()