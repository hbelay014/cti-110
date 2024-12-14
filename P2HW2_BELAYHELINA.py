# Your Name: Helina Belay
# Date: 10-03-2024
# P2HW2_GradesStatistics
# This program takes grades for six modules, stores them in a list, and displays statistics (lowest, highest, sum, average).

# Input: Gather grades for six modules
grades = []
for i in range(1, 7):
    grade = float(input(f"Enter grade for Module {i}: "))
    grades.append(grade)

# Calculate statistics
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

# Display results
print("\n------------Results------------")
print(f"{'Lowest Grade:':<20}{lowest_grade:.1f}")
print(f"{'Highest Grade:':<20}{highest_grade:.1f}")
print(f"{'Sum of Grades:':<20}{sum_of_grades:.1f}")
print(f"{'Average:':<20}{average_grade:.2f}")
print("-------------------------------")
