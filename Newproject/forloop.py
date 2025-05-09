# For loop
# The for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iteratable object.
# It is used to execute a block of code a fixed number of times or to iterate over a collected of iterable objects. 
# The for loop is a control flow statement that allows code to be executed repeatedly based on a conditional statement 

# for loop syntax:
# for variable in iterable:
#    # code block to be executed
# for example, the following code used a for loop to iterate over a list of numbers and print each number to the console

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
print("**********")
for number in range(6):
    print(number)

print("**********")

for number in range(3):
    print('Hello', number + 1)