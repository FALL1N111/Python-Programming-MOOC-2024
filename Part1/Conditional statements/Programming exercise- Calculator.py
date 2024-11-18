#ask users  for 3 nubmber and operation system! add, multiplay,subtract!
number1=int(input(f"Number 1: "))
number2=int(input(f"Number 2: "))
operation = input("Operation: ").strip().lower()
if operation == "multiply":
    print(f"{number1} * {number2} = {number1 * number2}")
if operation == "add":
    print(f"{number1} + {number2} = {number1 + number2}")
if operation == "subtract":
    print(f"{number1} - {number2} = {number1 - number2}")
