first= int(input("Enter first number: "))
second= int(input("Enter second number: "))
third= int(input("Enter third number: "))

if first > second:
    if first > third:
        print(f"{first} is greatest.")
    elif third > first:
        print(f"{third} is greatest.")
elif second > first:
    if second > third:
        print(f"{second} is largest.")
    elif third > second:
        print(f"{third} is greatest.")