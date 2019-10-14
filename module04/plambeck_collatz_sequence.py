# Lets the user type in an integer and keeps calling collatz() on that number
# until the function returns the value 1.

def collatz(number):
    if number % 2 == 0:             # If the number is even...
        print(number // 2)
        return number // 2
    elif number % 2 == 1:           # If the number is odd...
        print(3 * number + 1)
        return 3 * number + 1

print('Enter number:')

while True:
    # Detects whether the user types in a noninteger string
    try:
        num = int(input())
        while num != 1:
            num = collatz(num)
    except ValueError:
        print('You must enter an integer.')
    # Ends the loop
    else:
        break
