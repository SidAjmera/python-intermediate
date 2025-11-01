principal= input("Enter the principal value: ")
rate= input("Enter the rate of interest: ")
time = input("Enter amount of years: ")
interest= (int(principal) * int(rate) * int(time)) / 100
print("Your interst will be " + str(interest))