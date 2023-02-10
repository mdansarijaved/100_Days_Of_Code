import string
import random

alphabets = list(string.letters)

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*']

print("Welcome to passGod!")

passLetter = int(input("How many letters do you want in your password: "))
passSymbol =int( input("How many symbols do you want in your password: "))
passNum = int( input("How many number do you want in your password: "))


password=""

for i in range(1,passLetter+1):
    password += random.choice(alphabets)

for i in range(1,passSymbol+1):
    password += random.choice(symbols)

for i in range(1,passNum+1):
    password += random.choice(numbers)
    
print(f"Your password is {password}")


    
