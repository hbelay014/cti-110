# ----------------------------------------------------
# Program Name: Grade Calculator
# Author: BELAY
# Date: 10/10/2024
# Description: 
# This program takes the grades for six modules, calculates 
# the average, and determines the corresponding letter grade.
# It also displays the lowest, highest, and total of the grades.
# ----------------------------------------------------

# This program takes a number grade, determines the average, and displays the letter grade for the average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# Display the lowest, highest, total, and average
print(f"Lowest grade: {low}")
print(f"Highest grade: {high}")
print(f"Sum of grades: {total}")
print(f"Average grade: {avg:.2f}")

# Determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
