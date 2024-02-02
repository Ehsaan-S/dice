import random
#print main menu
print("main Menu")
print("1: Roll dice once")
print("2: roll dice 5 times")
print("3: Roll Dice 'n' times")
print("4: Roll dice until Snake Eyes")
print("Exit")

#menu selection
selection = input("Select an option (1-5)")
# action based on selection
if selection =="1":
def roll2Dice():
    dice1=random.randrange(1,7)
    dice2=random.randrange(1,7)
    return print ((dice1,dice2),"the sum is", dice1+dice2)

roll2Dice()

