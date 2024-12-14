# Program Name: Multiplication Table
# Author: [Your Last Name]
# Date: [Insert Current Date]
# Description: This program displays the multiplication table for a given integer from 1 to 12.
#              It handles positive integers, zero, and prompts the user to run the program again.
#              Negative numbers are not supported, and the program will display a message if a 
#              negative number is input.

def display_table(number):
    if number < 0:
        print("This program does not handle negative numbers.")
    else:
        # Use a for loop to display the multiplication table
        for i in range(1, 13):
            print(f"{number} * {i} = {number * i}")

def main():
    # Use a while loop to allow the user to run the program multiple times
    while True:
        try:
            # Input: Ask for an integer
            user_input = int(input("Enter an integer: "))

            # Display multiplication table or a message based on input
            display_table(user_input)

            # Ask if the user wants to run the program again
            repeat = input("Would you like to run the program again? (yes/no): ").strip().lower()

            if repeat != 'yes':
                print("Exiting program...")
                break  # Exit the loop and terminate the program

        except ValueError:
            print("Please enter a valid integer.")

# Call the main function
main()

