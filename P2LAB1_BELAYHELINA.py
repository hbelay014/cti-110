# Your Name
# Date
# P2LAB1_CircleCalculations
# This program calculates the diameter, circumference, and area of a circle given the radius.

import math

# Prompt the user for the radius
radius = float(input("What is the radius of the circle? "))

# Calculate diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# Display the results with specified formatting
print(f"The diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")
