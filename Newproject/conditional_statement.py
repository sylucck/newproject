# Conditional Statement
# This program checks if a number is positive, negative, or zero
# and prints the result.
# It also checks if the number is even or odd.
# The program uses if-elif-else statements to determine the result.
# The program uses the input() function to get user input.
# The program uses the int() function to convert the input to an integer.

#Temperature = int(input("Enter the temperature: "))
#if Temperature > 30:
#    print("it's hot")
#elif Temperature < 30:
   # print("it's cold")
#else:
   # print("It's a nice day")


#age = int(input("Enter your age here: "))
#if age >= 18:
 #   print("You are eligible to vote.")
#else:
 #   print("You are not eligible to vote.")


# Tenery operator
# The ternary operator is a shorthand way of writing an if-else statement.
# It is also known as the conditional expression.
# The syntax for the ternary operator is:
# value_if_true if condition else value_if_false
# The ternary operator is used to assign a value to a variable based on a condition.
# It is a one-liner that can be used to replace simple if-else statements.

# building a simple voters app using the ternary operator
#age = int(input("Enter your age here: "))
#message = "You are eligible to vote." if age >= 18 else "You are not eligible to vote."
#print(message)

# Logical operators
# Logical operators are used to combine conditional statements.
# The logical operators are:
# and, or, not
# The and operator returns True if both statements are true.
# The or operator returns True if at least one statement is True.
# The not operator reverses the result of the condition.
# The not operator returns True if the statement is false.
# The not operator returns False if the statement it true.
# The not operator is used to nagate a condition.

# building a simple loan processing app using the logical operators
#high_income = True
#good_credit = True

#if high_income and good_credit:
 #   print("You are eligible for a loan.")
#else:
 #   print("You are not eligible for a loan.")

#high_income = False
#good_credit = True

#if high_income and good_credit:
 #   print("You are eligible for a loan.")
#else:
  #  print("You are not eligible for a loan.")


#high_income = False
#good_credit = True

#if high_income or good_credit:
 #   print("You are eligible for a loan.")
#else:
 #   print("You are not eligible for a loan.")


high_income = True
good_credit = True
Student = True


if (high_income or good_credit) and not Student:
    print("You are eligible for a loan.")
else:
    print("You are not eligible for a loan.")


high_income = True
good_credit = True
Student = True

if not Student:
    print("You are eligible for a loan.")
else:
    print("You are not eligible for a loan")
