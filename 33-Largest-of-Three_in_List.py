mylist = []
for i in range(3):
    a = int(input("Enter a number: "))
    mylist.append(a)
if mylist[0] > mylist[1]:
    if mylist[0] > mylist[2]:
        print(f"{mylist[0]} is greatest.")
    else:
        print(f"{mylist[2]} is greatest.")
elif mylist[1] > mylist[0]:
    if mylist[1] > mylist[2]:
        print(f"{mylist[1]} is largest.")
    else:
        print(f"{mylist[2]} is greatest.")