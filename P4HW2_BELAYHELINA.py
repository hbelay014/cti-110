# ----------------------------------------------------
# Program Name: Employee Pay Calculator
# Author: [Your Last Name]
# Date: [Insert Current Date]
# Assignment: P4HW2
# Description:
# This program collects employee names, hours worked, and pay rates,
# calculates regular pay, overtime pay, and gross pay. 
# It continues until the user enters 'Done' for the employee's name.
# At the end, it displays totals for overtime, regular pay, and gross pay.
# ----------------------------------------------------

# Pseudocode:
# 1. Define a function `calculate_pay(hours_worked, pay_rate)` that:
#    a. Initializes overtime_hours, overtime_pay, regular_pay, and gross_pay to 0.
#    b. Checks if `hours_worked` is greater than 40:
#       i. If true, calculate overtime hours as `hours_worked - 40`.
#       ii. Set `regular_hours` to 40.
#       iii. Calculate overtime pay as `overtime_hours * pay_rate * 1.5`.
#    c. If false, set `regular_hours` to `hours_worked`.
#    d. Calculate regular pay as `regular_hours * pay_rate`.
#    e. Calculate gross pay as `regular_pay + overtime_pay`.
#    f. Return `regular_hours`, `overtime_hours`, `regular_pay`, `overtime_pay`, and `gross_pay`.

# 2. Define a `main()` function that:
#    a. Initializes `total_overtime_pay`, `total_regular_pay`, `total_gross_pay`, and `total_employees` to 0.
#    b. Enters a `while True` loop that continues until the user enters 'Done' for the employee name:
#       i. Prompt the user to input the employee's name.
#       ii. If the name is 'Done', exit the loop.
#       iii. Otherwise, ask the user for `hours_worked` and `pay_rate`.
#       iv. Call `calculate_pay(hours_worked, pay_rate)` and store the returned values.
#       v. Print the employee's name and their pay details in a formatted table.
#       vi. Add `overtime_pay`, `regular_pay`, and `gross_pay` to their respective total variables.
#       vii. Increment `total_employees` by 1.
#    c. After exiting the loop, print the total number of employees and the totals for overtime, regular, and gross pay.

# 3. Call the `main()` function to run the program.

def calculate_pay(hours_worked, pay_rate):
    """Calculate regular pay, overtime pay, and gross pay."""
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = 0
    gross_pay = 0
    
    # Check if employee worked more than 40 hours for overtime
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
        overtime_pay = overtime_hours * pay_rate * 1.5
    else:
        regular_hours = hours_worked
    
    # Calculate regular pay and gross pay
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay
    
    return regular_hours, overtime_hours, regular_pay, overtime_pay, gross_pay

def main():
    total_overtime_pay = 0
    total_regular_pay = 0
    total_gross_pay = 0
    total_employees = 0

    while True:
        # Get employee name
        employee_name = input("Enter employee's name or 'Done' to terminate: ")
        
        # Check if user wants to terminate the program
        if employee_name.lower() == 'done':
            break
        
        # Get hours worked and pay rate
        hours_worked = float(input(f"How many hours did {employee_name} work? "))
        pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
        
        # Calculate pay
        regular_hours, overtime_hours, regular_pay, overtime_pay, gross_pay = calculate_pay(hours_worked, pay_rate)
        
        # Display employee pay details
        print(f"\nEmployee name: {employee_name}")
        print(f"{'Hours Worked':<12} {'Pay Rate':<8} {'OverTime':<8} {'OverTime Pay':<12} {'RegHour Pay':<12} {'Gross Pay':<10}")
        print(f"{regular_hours + overtime_hours:<12.1f} {pay_rate:<8.2f} {overtime_hours:<8.1f} {overtime_pay:<12.2f} {regular_pay:<12.2f} {gross_pay:<10.2f}\n")
        
        # Update totals
        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay
        total_employees += 1

    # Display totals after all employees are entered
    print(f"Total number of employees entered: {total_employees}")
    print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
    print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
    print(f"Total amount paid in gross: ${total_gross_pay:.2f}")

# Run the main function
main()

