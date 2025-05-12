# while loops
# This program uses a while loop to print a pattern of numbers
# The outer loop iterates over the range of numbers from 1 to 5


while True:
    command = input('>')
    print("ECHO", command)
    if command.lower() == 'quit':
        break

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")