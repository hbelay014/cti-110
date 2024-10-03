# Author: Helina Belay
# Date: 09-27-2024
# Description: This program converts an amount of money into dollars, quarters, dimes, nickels, and pennies.

def money_to_coins(amount):
    # Convert to cents by multiplying by 100
    cents = int(amount * 100)
    
    # Calculate number of dollars
    dollars = cents // 100
    cents = cents % 100
    
    # Calculate number of quarters
    quarters = cents // 25
    cents = cents % 25
    
    # Calculate number of dimes
    dimes = cents // 10
    cents = cents % 10
    
    # Calculate number of nickels
    nickels = cents // 5
    cents = cents % 5
    
    # Remaining cents are pennies
    pennies = cents
    
    # Create a list to store the output
    output = []
    
    # Append results to the output list, checking for singular/plural forms
    if dollars > 0:
        output.append(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        output.append(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        output.append(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        output.append(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        output.append(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")
    
    # Return 'No change' if there is nothing to display
    if not output:
        return "No change"
    
    # Join the list elements into a single string separated by new lines
    return '\n'.join(output)

# Get user input
amount = float(input("Enter the amount of money as a float: "))

# Display the result
print(money_to_coins(amount))
