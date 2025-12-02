string = input("Enter 2 or more letters: ")
amount = len(string)
for i in range(amount - 1, -1, -1):
    print(string[i], end = "")
print("")  