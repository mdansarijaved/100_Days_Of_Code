print("Welcome to javed's pizza.")
size = input("What size pizza do you want. S , M or L: ")

peporoni = input("Do you want peporoni on your pizza. Y or N: ")

extra_cheese = input("Do you want extra cheese on your pizza. Y or N: ")

bill = 0

if size == "S":
    bill = 15
    if peporoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill = 20
    if peporoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill +=1
elif size == "L":
    bill = 25
    if peporoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
else:
    print("This size doesn't exists.")
    
print(f"Your total bill for your pizza of sixe {size} is {bill}$ ")