# Short circuiting in Python
# Short-circuiting is a programming technique where the second argument is not evaluated if the first argument is sufficient to determine the value of the expression.
# In Python, short-circuiting occurs with the and and or logical operators.
# The and operator returns True if both statements are true. If the first statement is false, the second statement is not evaluated.
# The or operator returns True if at least one statement is True. If the first statement is true, the second statement is not evaluated.
# Short-circuiting is a performance optimization technique that can be used to improve the efficiency of the code.
# It can also be used to prevent errors in the code by avoiding the evaluation of expressions that may contain errors.


high_income = True
good_credit = True
Student = False


if high_income and good_credit and Student:
    print("You are eligible for a loan.")
else:
    print("You are not eligible for a loan.")

high_income = False
good_credit = True
Student = False

if high_income or good_credit and Student:
    print("You are eligible for a loan.")
else:
    print("You are not eligible for a loan.")