print("Welcome to the tip calculator!")
# ask the user for bill amount
bill = float(input("What was the total bill? $"))
# ask the percentage of tip user is willing to pay
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# ask how many people will split the bill between
people = int(input("How many people to split the bill? "))
# calculate the amount each person pay
pay = (bill/people) * (1+tip/100)
#printing the final amount
print(f"Each person should pay: {round(pay,2)} $\nThank you! ")
