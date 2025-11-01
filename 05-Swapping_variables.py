number1= input("Choose a number: ")
number2= input("Choose another number: ")
print("You said: number 1 is " + (number1) + " and number 2 is " + (number2))
number1, number2 = number2, number1
print(f"Now, number 1 is {number1} and number 2 is {number2}!")