# formating a string 


age = int(input("Enter your age : "))
Name = input("Enter your name: ")

txt = "Hello I'm {} and my age is {} ."

print(txt.format(Name,age))



# here is another example 


price = 4
print(f"One candy costs {price} dollars. ")

quantity = int(input("How many candies do you want: "))

total_price = price * quantity

txt = "Your total bill is {1} dollars for {0} candies you have bought."

print(txt.format(quantity,total_price))



# To use double quotes in print statement there is two ways for this in python 
#1st way 

print('Hello budyy "what the fuck"')

#2nd way is to use escape charater 

print("how are you \"buddy\" fuck you na bro who the hell are you bro.")