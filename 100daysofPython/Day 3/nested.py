height = int(input("Enter your height in cm : "))
bill = 0


if height >= 120:
    print("you can ride rollercoaster.")
    
    age = int(input("Enter your age : "))
    
    if age <= 12:
        
        bill = 5
        
        print(f"your current bill is {bill}$ .")
        
    elif age <= 18:
        
        bill = 7
        
        print(f"your current bill is {bill}$ .")
        
    else:
        
        bill = 12
        
        print(f"your current bill is {bill}$ .")
        
    photo = input("Do you want your photo. y or n ")
    
    if photo == "y":
        bill = bill + 3
        print(f"your total bill will be {bill}$ . ")
        
    else:
        print(f"your total bill will be {bill}$ .")
        
        
else:
    
    print("you can't ride rollercoaster.")
