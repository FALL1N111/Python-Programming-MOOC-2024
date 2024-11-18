#ask for a number!
number = int(input('Please type in a nummber: '))
if number < 0:
    print(f"The absolute value of this number is {number * -1}")
if number >= 0:
    print(f"The absolute value of this number is {number}")