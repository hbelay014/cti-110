# Your Name: Helina Belay
# Date:10-03-2024
# P2HW1_TravelExpenses
# This program calculates and displays travel expenses with formatted output.

# Input: Gather user information
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display formatted output
print("\n------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:.2f}")
print(f"{'Fuel:':<20}${gas:.2f}")
print(f"{'Accommodation:':<20}${accommodation:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print("----------------------------------------")
print(f"{'Remaining Balance:':<20}${remaining_balance:.2f}")
