# Break and continue in for loop
# The break statement is used to exit a loop prematurely, while the continue statement is used to skip the current iteration and move to the next iteration.

for number in range(1, 20, 5):
    if number == 15:
        break
    print("Hello", number, number * "*")

print("**********")

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Success")
        break

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Success")
else:
    print("Attempted 3 times")


