course = "Python Programming"
print(len(course))
print(course[0])
print(course[-4])
print(course[6])
print("Hello  \" world")
print('welcome to my world of homes \\ ')
print('welcome to the new line of codes \n I\'m watching you')
#
# \' backslash escapes the single quote
# \" backslash escapes the double quote
# \\ backslash escapes the backslash itself
# \n backslash escapes the new line character
# \t backslash escapes the tab character
# \b backslah escapes the backspace character

# concatinating strings
# strings can be concatenated using the + operator
first_name = "Sylvester"
last_name = "Nkwonta"
full_name = first_name + " " + last_name
print(full_name)

# using f-string to format strings
age = 30
print(f"{len(full_name)} {last_name} is {age} years old")

# using python methods
# string methods are used to manipulate strings
# string methods are used to perform operations on strings
course = "Python Programming is the best programming language. A language that has been in use for over"

print(course.upper())  # convert to uppercase
print(course.lower())  # convert to lowercase
print(course.title())  # convert to title case
print(course.casefold())  # convert to casefold
print(course.capitalize())  # convert to capitalized case
# remove whitespace from the beginning and end of the string
print(course.strip())
print(course.lstrip())  # remove whitespace from the beginning of the string
print(course.rstrip())  # remove whitespace from the end of the string
print(course.replace("Python", "Java"))  # remove and replace a string
print(course.split())  # split the string into a list of strings
# split the string into a list of strings using space as the separator
# find the index of the first occurrence of a string
print(course.find("p"))
print(course.index("n"))  # find the index of the string
print(course.count("n")) # count the number of occurrences of a string
print(course.startswith("P")) # check if the string starts with a string
print(course.endswith("g")) # check if the string ends with a string
print(course.isalnum()) # check if the string is alphanumeric
print('pro' in course) # check if a string is in another string
print('pro' not in course) # check if a string is not in another string
print(course.isalpha()) # check if the string is alphabetic
print(course.isdigit()) # check if the string is a digit
print(course.isnumeric()) # check if the string is numeric 
print(course.isdecimal()) # check if the string is decimal
print(course.isidentifier()) # check if the string is an identifier

#Numbers
# Interger is a whole number, positive or negative, without decimals, of unlimited length
# Intergers are used to represent whole numbers 

x = 5 # interger
x = 1.1 # float
 # a + bi, complex number where i is the imaginary unit
# in python, complex numbers are represented as a + bj,  where a is the real part and b is the imaginary part
x = 1 + 2j # comeplex number

#mathematical operations
# adddition, subtraction, muultiplication, division, exponentiation, floor division, modulus
print (5 + 2) # addition
print (5 - 2) # subtraction
print (5 * 2) # multiplication
print (5 / 2) # division (gets you a float)
print (5 // 2) # floor division (gets you an interger)
print ( 5 % 2) # modulus (gets you the remainder of the division)
print (5 ** 2) # exponentiation (gets you the power of the number)
print (5 ** 0.5) # square root of a number
print (5 ** 3) # cube of a number

# augmented assignment operators
# +=, -=, *=, /=, //=, %=, **=
# these operators are used to perform operations on variables and assign the result to the variable
x = 5
x += 2 # x = x + 2 
print(x) # 7
x -= 2 # x = x - 2
print(x) # 5

# mathematical functions
# abs(), round(), pow(), min(), max(), sum(), divmod()
# abs() returns the absolute value of a number
# round() returns the rounded value of a number
# pow() returns the power of a number
# min() returns the minimun value of a list of numbers 
# max() returns the maximum value of a list of numbers
# sum() returns the sum of a list of numbers
# divmod() returns the qupotient and remainder of a division
# divmod(5, 2) returns (2, 1) # 2 is the quotient and 1 is the remainder
# divmod(5, 0) returns (inf, 0) # inf is the infinity value
print(round(5.5)) # 6
print(abs(-5)) # 5
print(pow(5, 2)) # 25
print(min(5, 2, 3, 4)) # 2
print(max(5, 2, 3, 4)) # 5
print(sum([5, 2, 3, 4])) # 14
print(divmod(5, 2)) # (2, 1)
print(divmod(6, 1)) # (inf, o)