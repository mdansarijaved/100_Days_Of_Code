num_char = str(len(input("what is your name? ")))

print(type(num_char))

print("Your name has "+ num_char + " characters in it. ")

# to check the data type of a variable 

a = 283
print(type(a))


print(70.3 + float("837.39"))

print(str(123)+ str(3848))


# mathematical operators 

3-5
4+4
4*3
3/5
3**2 #this is used to raise a number to a power ( 3^2 )

# Priority in python for mathematical operators follow pedmas
# () -> **  -> / or * -> + or - 


#number manipulation 

# to round the decimal number 

print(round(10/3,2))

print(8//3) #floor division this will do the work of int(8/3)


# f-string
age =18
name = "javed"

print(f"your age is {age} and your name is {name}")