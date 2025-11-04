first = (input("Enter the first number: "))
second = (input("Enter the second number: "))
operator = input("Enter the operator: ")
try: 
    result = eval(first + operator + second)
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Dividing by zero is not allowed. Please try again.")
except:
    print("Oops. Something went wrong.")