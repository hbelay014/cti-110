# Your Name: Helina Belay
# Date09/26/2024
# Assignment Name: P1HW2_HelinaBelay
# This program calculates and displays travel expenses

# Pseudocode:
# 1. Prompt the user to enter their budget and store the value.
# 2. Prompt the user to enter their travel destination and store the value.
# 3. Prompt the user to enter the amount they will spend on gas and store the value.
# 4. Prompt the user to enter the amount they will spend on accommodation and store the value.
# 5. Prompt the user to enter the amount they will spend on food and store the value.
# 6. Calculate the total expenses by summing gas, accommodation, and food expenses.
# 7. Subtract the total expenses from the budget to find the remaining balance.
# 8. Display the travel destination, initial budget, each of the expenses, and the remaining balance.

# Getting user inputs
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas_expense = float(input("How much do you think you will spend on gas? "))
accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))
food_expense = float(input("Last, how much do you need for food? "))

# Calculating total expenses and remaining balance
total_expenses = gas_expense + accommodation_expense + food_expense
remaining_balance = budget - total_expenses

# Displaying the results
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print(f"\nFuel: {gas_expense}")
print(f"Accommodation: {accommodation_expense}")
print(f"Food: {food_expense}")
print(f"\nRemaining Balance: {remaining_balance}")

