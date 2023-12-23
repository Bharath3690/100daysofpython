import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

img=[rock,paper,scissors]
print("Welcome to Rock, Paper, Scissors!")
user_chc=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
print(user_chc)
print(img[user_chc])
comp_choice=random.randint(0,2)
print(comp_choice)
print(img[comp_choice])
if user_chc>=3 or user_chc<0:
  print("Invalid nuber,you lose!")
elif user_chc==0 and comp_choice==2:
  print("you win!")
elif comp_choice==0 and user_chc==2:
  print("You lose!")
elif user_chc<comp_choice:
  print("You lose!")
elif user_chc>comp_choice:
  print("You win!")
elif user_chc==comp_choice:
  print("match drawn")
