import random
test_seed = input("Press enter to toss a coin ")
random.seed(test_seed)
testseed = random.randint(0,1)
if testseed == 0 :
 print("Heads")
else:
 print("Tails")