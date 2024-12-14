# Your Name: Helina Belay
# Date: 10-03-2024
# P2LAB2_VehicleMPG
# This program calculates the gallons of gas needed for a vehicle to travel a specified number of miles.

# Dictionary containing vehicle MPG values
vehicle_mpg = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

# Creating a variable that holds all the keys in the dictionary
keys = vehicle_mpg.keys()
print(keys)

# Prompt the user to enter a vehicle name
vehicle_name = input("Enter a vehicle to see its mpg: ")

# Check if the vehicle exists in the dictionary
if vehicle_name in vehicle_mpg:
    mpg = vehicle_mpg[vehicle_name]
    print(f"The {vehicle_name} gets {mpg} mpg.")
    
    # Prompt the user to enter the number of miles
    miles = float(input(f"How many miles will you drive the {vehicle_name}? "))
    
    # Calculate the gallons of gas needed
    gallons_needed = miles / mpg
    
    # Display the gallons needed, rounded to two decimal places
    print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle_name} {miles} miles.")
else:
    print(f"Vehicle '{vehicle_name}' not found in the list.")
