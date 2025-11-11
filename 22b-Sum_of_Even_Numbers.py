N = int(input("Enter a number: "))
total = 0
for i in range(2, N+1, 2):
    total += i
print(f"Sum of even numbers: {total}")