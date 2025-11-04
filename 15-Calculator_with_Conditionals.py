first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
operator = input("Enter the operator: ")

if operator == "+":
    number = first + second
    print(f"Result: {number}")
elif operator == "-":
    number = first - second
    print(f"Result: {number}")
elif operator == "*":
    number = first * second
    print(f"Result: {number}")
elif operator == "/":
    if second != 0:
        number = first/second
        print(f"Result: {number}")
    if second == 0:
        print("Sorry, dividing by zero is not possible. Please try again.")
elif operator == "%":
    number = first % second
    print(f"Result: {number}")
else:
    print("Invalid operator. Please try again.")