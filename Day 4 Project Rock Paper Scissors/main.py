import random
rock = '''
    ______
---'   _____)
      (______)
      (______)
      (______)
---.__(___)
'''

paper = '''
    _______
---'   ____)_____
          _________)
          __________)
         _________)
-----._________)
'''

scissors = '''
    _______
---'   ____)______
          ________)
       ___________)
      (____)
---.__(___)
'''


print("Welcome to rock paper and scissors")
print("Enter 0 for rock, 1 for paper, 2 for scissors")
choice = int(input("Enter your choice: "))
if choice == 0:
    print(f"You chose: rock \n{rock}")
elif choice == 1:
    print(f"You chose: paper \n{paper}")
else:
    print(f"You chose: scissors \n{scissors}")

comp_choice = random.randint(0, 2)
if comp_choice == 0:
    print(f"Computer Chose: rock \n{rock}")
elif comp_choice == 1:
    print(f"Computer Chose: paper \n{paper}")
else:
    print(f"Computer Chose: scissors \n{scissors}")

#losing condition:
if (choice == 0 and comp_choice == 1) or (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 0):
    print("You lost")

elif (comp_choice == 0 and choice == 1) or (comp_choice == 1 and choice == 2) or (comp_choice == 2 and choice == 0):
    print("Congratulations! You have won.")




