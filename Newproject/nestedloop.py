# Nested loops
# This program uses nested loops to print a pattern of numbers
# The outer loop iterates over the range of numbers from 1 to 5
# The inner loop iterates over the range of numbers from 1 to the current value of the outer loop variable i

for x in range(5):
    for y in range(3):
        print(f"Outer loop: {x}, Inner loop: {y}")