import random 
import module

random_integer = random.randint(1,5)
print(module.myage)

user_input = int(input("Enter a number between 1 to 5: "))

if random_integer == user_input:
    print(f"your guess {random_integer} is right, you've won the mega lottery.")
else:
    print(f"winning number was {random_integer}, better luck next time")

