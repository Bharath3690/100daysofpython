print("Welcome to tip calculator")
bill=float(input("What is the total bill?"))
tip_percentage=float(input("what percentage tip would you like to give? 10, 12, or 15? "))
members=float(input("How many people to split the bill?"))
input("Each person should pay: ")
amount=float((bill/members)*tip_percentage)
print(round(amount,2))

