first= int(input("Enter first number: "))
second= int(input("Enter a differenr number: "))
third= int(input("Enter a different number: "))

if first > second:
    if first > third:
        print(f"{first} is greatest.")
    else:
        print(f"{third} is greatest.")
elif second > first:
    if second > third:
        print(f"{second} is largest.")
    else:
        print(f"{third} is greatest.")