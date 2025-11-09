number= input("Enter a number: ")
r = float(number)%2

if r == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")