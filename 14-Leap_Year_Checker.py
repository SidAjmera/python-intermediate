year = int(input("Enter a year: "))

r = year%4

if r != 0:
    print(f"{year} is not a leap year.")
elif r == 0:
    y = year%100
    if y != 0:
        print(f"{year} is not a leap year.")
    elif y == 0:
        x = year%400
        if x != 0:
            print(f"{year} is not a leap year.")
        elif x == 0:
            print(f"{year} is a leap year.")