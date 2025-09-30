#step 1 roll the dice and ask to user to select
# 2 remember invalid choice
# 3 if yes then show 2 random number
# 4 if no then terminate the 
# thanks for playing

import random

while True:
    user = input("Roll The Dice? (y/n):  ").lower()
    if user == "y" :
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"({die1},{die2} )")
    elif user == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
