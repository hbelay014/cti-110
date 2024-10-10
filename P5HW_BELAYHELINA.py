# ----------------------------------------------------
# Program Name: Math Quiz
# Author: BELAY
# Date: 10/09/2024
# Assignment: P5HW
# Description:
# This program presents a math quiz with options for addition and subtraction.
# Users are prompted to guess the result of random math problems and receive
# feedback on their guesses. The program terminates only when the user selects
# option 3 from the menu.
# ----------------------------------------------------

import random

def addition_quiz():
    """Generates two random numbers and quizzes the user on their sum."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    print(f"\n{num1} + {num2}")
    
    correct_answer = num1 + num2
    guesses = 0
    
    while True:
        user_answer = int(input("Enter answer: "))
        guesses += 1
        
        if user_answer < correct_answer:
            print("Sorry, guess is too low.")
        elif user_answer > correct_answer:
            print("Sorry, guess is too high.")
        else:
            print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses: {guesses}")
            break

def subtraction_quiz():
    """Generates two random numbers and quizzes the user on their difference."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    print(f"\n{num1} - {num2}")
    
    correct_answer = num1 - num2
    guesses = 0
    
    while True:
        user_answer = int(input("Enter answer: "))
        guesses += 1
        
        if user_answer < correct_answer:
            print("Sorry, guess is too low.")
        elif user_answer > correct_answer:
            print("Sorry, guess is too high.")
        else:
            print(f"Congratulations!!!! Your answer is correct.\nNumber of guesses: {guesses}")
            break

def main():
    """Displays the main menu and manages the quiz options."""
    while True:
        print("\nMAIN MENU")
        print("---------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        
        try:
            choice = int(input("\nPlease choose one of the menu options: "))
            
            if choice == 1:
                addition_quiz()
            elif choice == 2:
                subtraction_quiz()
            elif choice == 3:
                print("Thank you for playing...\nBye!!")
                break
            else:
                print("Error: Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Error: Please enter a valid number.")

# Call the main function to run the program
main()
