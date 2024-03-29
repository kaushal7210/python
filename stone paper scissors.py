import random
testseed = print("What do you chose?")
testseed = input("Type 1 for rock, 2 for paper, 3 for scissors.\n")

if testseed == "1" :
 print(''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif testseed == "2" :
 print('''
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif testseed == "3" :
  print('''
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) 
''')
else :
  print("Invalid input")

print("Computer chose:")
testchoice = random.randint(1,3)
if testchoice == 1 :
 print(''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif testchoice == 2 :
 print('''
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
else :
  print('''
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) 
''')
if testseed == "1" and testchoice == 1 or testseed == "2" and testchoice == 2 or testseed == "3" and testchoice == 3:
   print("It's a draw")
elif testseed == "1" and testchoice == 2 or testseed == "2" and testchoice == 3 or testseed == "3" and testchoice == 1:
   print("You lose.")
elif testseed == "2" and testchoice == 1 or testseed == "3" and testchoice == 2 or testseed == "1" and testchoice == 3:
   print("You win.")
else :
   print("Computer wins.")