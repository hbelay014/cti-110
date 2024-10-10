# ----------------------------------------------------
# Program Name: Self-Checkout Change Calculator
# Author: BELAY
# Date: 10/09/2024
# Assignment: PSLAB
# Description:
# This program simulates a self-checkout machine, calculates the change 
# owed to the customer, and displays the amount of dollars, quarters, 
# dimes, nickels, and pennies required.
# ----------------------------------------------------

import random

# Function to calculate and display change breakdown
def disperse_change(change):
    """Calculates the number of dollars, quarters, dimes, nickels, and pennies."""
    
    # Convert change into cents to avoid floating-point issues
    cents = int(round(change * 100))
    
    # Calculate dollars
    dollars = cents // 100
    cents %= 100
    
    # Calculate quarters (25 cents)
    quarters = cents // 25
    cents %= 25
    
    # Calculate dimes (10 cents)
    dimes = cents // 10
    cents %= 10
    
    # Calculate nickels (5 cents)
    nickels = cents // 5
    cents %= 5
    
    # Remaining cents are pennies
    pennies = cents
    
    # Display the breakdown of change
    if dollars > 0:
        print(f"{dollars} Dollar" + ("s" if dollars > 1 else ""))
    if quarters > 0:
        print(f"{quarters} Quarter" + ("s" if quarters > 1 else ""))
    if dimes > 0:
        print(f"{dimes} Dime" + ("s" if dimes > 1 else ""))
    if nickels > 0:
        print(f"{nickels} Nickel" + ("s" if nickels > 1 else ""))
    if pennies > 0:
        print(f"{pennies} Penn" + ("ies" if pennies > 1 else "y"))

def main():
    """Main function to simulate self-checkout and calculate change."""
    
    # Generate a random float value for the total owed
    total_owed = round(random.uniform(0.81, 100.00), 2)
    
    # Display the total owed
    print(f"You owe ${total_owed:.2f}")
    
    # Prompt user to enter the amount of cash they will put in the self-checkout
    cash_given = float(input("How much cash will you put in the self-checkout? "))
    
    # Calculate the change owed
    change = cash_given - total_owed
    
    # Display the change owed
    print(f"Change is: ${change:.2f}")
    
    # Call the disperse_change() function to display the breakdown of change
    disperse_change(change)

# Call the main function to run the program
main()
