print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill: "))

tip_percentage = int(input("What percentage tip would you like to give? 10% , 12% , 15% ?"))

total_payer = int(input("How many people to split the bill: "))

pay_for_per_person = round( ((total_bill + (total_bill * tip_percentage/100)) / 7),2)

print(f"each person should pay {pay_for_per_person} .")