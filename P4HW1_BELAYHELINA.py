# ----------------------------------------------------
# Program Name: Score Average and Grade Calculator
# Author: BELAY
# Date: 10/08/2024
# Assignment: P4HW1
# Description:
# This program asks the user to input a certain number of scores,
# validates the scores, calculates the average after dropping 
# the lowest score, and displays the letter grade for the average.
# ----------------------------------------------------

def calculate_letter_grade(average):
    """This function calculates the letter grade based on the average score."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # Ask user for number of scores
    num_scores = int(input("Enter the number of scores you would like to enter: "))
    scores = []

    # Collect the scores
    for i in range(num_scores):
        while True:
            try:
                score = float(input(f"Enter score {i + 1}: "))
                
                # Validate if the score is between 0 and 100
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Invalid score. Please enter a score between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Remove the lowest score
    lowest_score = min(scores)
    scores.remove(lowest_score)
    print(f"Lowest score {lowest_score} has been dropped.")

    # Calculate the average of the remaining scores
    average = sum(scores) / len(scores)

    # Display the average and letter grade
    print(f"Average after dropping the lowest score: {average:.2f}")
    letter_grade = calculate_letter_grade(average)
    print(f"Letter grade: {letter_grade}")

# Call the main function
main()
