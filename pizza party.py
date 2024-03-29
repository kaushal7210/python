print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S" :
   if add_pepperoni == "Y" :
    bill += 2
   else :
    bill += 15
elif size == "M" : 
 if add_pepperoni == "Y" : 
  bill += 3
 else :
   bill += 20
elif size == "L":
  bill += 25 
  if add_pepperoni == "Y" :
    bill += 3
if extra_cheese == "Y" :
 bill += 1
 print(f"Your final bill is ${bill}.")
else :
 bill += 0
print(f"Your final bil is ${bill}.")