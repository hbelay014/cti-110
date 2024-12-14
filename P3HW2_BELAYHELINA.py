# ----------------------------------------------------
# Program Name: Salary Calculator
# Author: BELAY
# Date: 10/10/2024
# Description: 
# This program calculates the gross pay of an employee, 
# taking into account regular hours and overtime hours.
# It displays the employee name, hours worked, pay rate,
# overtime pay, regular pay, and total gross pay.
# ----------------------------------------------------

# Pseudocode
# 1. Ask the user to enter the employee's name.
# 2. Ask the user to enter the number of hours worked this week.
# 3. Ask the user to enter the employee's pay rate.
# 4. If hours worked are more than 40:
#     a. Calculate overtime hours.
#     b. Calculate regular pay for 40 hours.
#     c. Calculate overtime pay at 1.5 times the pay rate for overtime hours.
#     d. Calculate the total gross pay.
# 5. If hours worked are 40 or less:
#     a. Calculate regular pay for the hours worked.
#     b. No overtime pay is applied.
# 6. Display the employee's name, hours worked, overtime hours, overtime pay, regular pay, and gross pay.

# Step 1-3: Input employee's name, hours worked, and pay rate
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Initialize overtime variables
overtime_hours = 0
overtime_pay = 0

# Step 4-5: Determine if overtime applies and calculate pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    regular_hours = hours_worked
    regular_pay = regular_hours * pay_rate

# Step 6: Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display the results
print(f"\nEmployee name: {employee_name}")
print(f"Hours Worked: {hours_worked:.1f}")
print(f"Pay Rate: {pay_rate:.2f}")
print(f"Overtime Hours: {overtime_hours:.1f}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Regular Pay: ${regular_pay:.2f}")
print(f"Gross Pay: ${gross_pay:.2f}")
