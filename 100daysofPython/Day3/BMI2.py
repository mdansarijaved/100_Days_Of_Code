weight = int(input("Enter you weight in kg: "))
height = float(input("Enter your height in meters: "))
Body_mass_index = (weight/height**2)

if Body_mass_index <= 18.5:
    print(f"your BMI is {Body_mass_index} and you're underweight.")
elif Body_mass_index <=25:
    print(f"you BMI is {Body_mass_index} and your weight is normal.")
elif Body_mass_index <=30:
    print(f"your BMI is {Body_mass_index} and you're overweight.")
elif Body_mass_index<=35:
    print(f"your BMI is {Body_mass_index} and you're obese.")
else:
    print(f"your BMI is {Body_mass_index} and you're clinically obese.")