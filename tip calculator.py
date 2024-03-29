# tip calculator
print("Welcome to the tip calculator")
bill = input("What was the total bill?")
tip = input("What percentage tip would you like to give?")
people = input("how many people to split the bill")
amount = (int(bill) + (int(tip) / 100) * int(bill)) / int(people)
print(f"each person should pay: {amount}")