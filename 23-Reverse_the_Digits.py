num = int(input("Enter a number with 3 or more digits: "))
reversed = 0
while num != 0:
    remainder = num % 10
    num = num // 10
    reversed = reversed * 10 + remainder
print(f"Reversed: {reversed}")

    