# -----Calculating Exponent-----
# get the base and exponent from the user
base = int(input("Enter an integer as the base value:"))
exponent = int(input(" Enter an integer as the exponent:"))
#Calculate the result of raising the base of the power of the exponent

result = base ** exponent
#print the result
print (f"{base} raised to the power of {exponent} is {result}!!")
# -----Addition and subtraction-----
# Get three integers from the user
start_integer =int(input("\nEnter a starting integer:"))
add_integer =int(input("Enter an integer to add:"))
subtract_integer = int(input("Enter an integer to subtract:"))
#perform the addition and subtraction
final_result = start_integer+add_integer-subtract_integer
# print the final result
print(f"{start_integer}+{add_integer}-{subtract_integer} is equal to {final_result}") 
