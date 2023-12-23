# leap year
# Which year do you want to check?
# year = int(input())
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# if year%4==0:
#   if year%100==0:
#     if year%400==0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")



# pizza order dlivry 
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# if size=="S":
#   bill=15
#   if add_pepperoni=="Y":
#     bill=15+2
#   else:
#     bill=15
# elif size=="M":
#   bill=20
#   if add_pepperoni=="Y":
#     bill=20+3
#   else:
#     bill=20
# elif size=="L":
#   bill=25
#   if add_pepperoni=="Y":
#     bill=25+3
#   else:
#     bill=25
# if extra_cheese=="Y":
#   bill += 1

# print(f"Your final bill is: ${bill}.")
  

# Love calculator
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name=name1 + name2
a=name.lower()
T=a.count("t")
R=a.count("r")
U=a.count("u")
E=a.count("e")
Total=str(T+R+U+E)
Total_1=str(a.count("l")+a.count("o")+a.count("v")+a.count("e"))
love=Total+Total_1
love_score=int(love)
if love_score<10 or love_score>90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40<love_score<50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}, you are just friends.")
