print("Welcome to Truelove.com check your love score.")

person1 = input("Enter your name: ")
person2 = input("Enter your lover Name: ")

person1 = person1.lower()
person2 = person2.lower()

combined = person1 + person2

true = combined.count('t') +combined.count('r') + combined.count('u') + combined.count('e')
love = combined.count('l') +combined.count('o') + combined.count('v') + combined.count('e')

total = true * 10 + love

if total <= 10 or total >= 90:
    print(f"Your love score is {total}, you guys are like coke and mentos. ")
elif total >= 40 and total <= 50:
    print(f"Your love score is {total}, these guys are born to together. ")
else:
    print(f"Your love score is {total}. these guys are born to be together happy gay life ")
    