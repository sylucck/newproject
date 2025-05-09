# Chaining comparison operators
# In Python, you can chain comparison operators  together to creat more complex expressions.
# For example, you can use the following syntax to check if a number is between two values:
# if 10 < x < 20:
#   print("x is between 10 and 20")
# This is equivalent to the following expression:
# if x > 10 and x < 20:
#  print("x is between 10 and 20")
# Chaining comparison operators can make your code more readable and easier to understand.
# It can also help you avoid using unnecessary parentheses and make your code more concise.

# age should be between 18 and 65

age = int(input("Enter your age:"))
if 18 < age < 65:
    print("You are eligible to work.")
else:
    print("You are not eligible to work.")
