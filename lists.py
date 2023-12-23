# states_of_india=["Andhrapradsh","West Bengal","Telangana","Tamilnadu"]
# states_of_india[1]="Bihar"
# # print(states_of_india)
# states_of_india.append("Kerala")
# # print(states_of_india)
# states_of_india.extend(["himachal","punjab","nagaland"])
# print(states_of_india)

# names = names_string.split(", ")
# # The code above converts the input into an array seperating
# #each name in the input by a comma and space.
# # 🚨 Don't change the code above 👆
# random_name=random.randint(0,len(names)-1)
# print(f"{names[random_name]} is going to buy the meal today!")

# dirty_dozen=["potato","tomato","apple","bananana"]
# fruits=["apple","banana"]
# vegetables=["potato","tomato"]
# # dirty_dozen=[fruits,vegetables]  nested lists
# print(dirty_dozen)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])