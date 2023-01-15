import math 
import random
print('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.')
user_choice = int(input())
ran_int = random.randint(0,2)

if user_choice == ran_int:
    print('Draw')
elif user_choice == 0 and ran_int ==1: 
    print("you loose, computer wins")
elif user_choice == 0 and ran_int ==2:
    print("you win")
elif user_choice == 1 and ran_int ==0:
    print("you win")
elif user_choice == 1 and ran_int ==2:
    print("you loose, computer wins")
elif user_choice == 2 and ran_int == 0: 
    print("You Loose, computer wins")
elif user_choice == 2 and ran_int == 1: 
    print("you win")
else: 
    print("invalid input")
