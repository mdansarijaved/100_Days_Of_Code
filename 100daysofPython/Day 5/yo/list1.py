# list in python 

# Lists are one of 4 built-in data types in Python used to 
# store collections of data, the other 3 are Tuple, Set, and Dictionary, 
# all with different qualities and usage.

Friends = ["aman","shivesh","musdick","harsh","garuav","shashwat"]

print(Friends)
print(len(Friends))

# a list can contain different data types 

list1 = [1,2,3,4,5,6]
list2 = [True,False,False]
list3 = ["aap","tum","tu"]
list4 = ["aap",1,False]
print(type(list4))


# accessing list elements 

print(list4[2])

#accessing list using negative indexing

print(list4[-1])

#accessing list elements in a range 

print(Friends[1:5])

# checking if the item exist in the list 

if "harsh" in Friends:
    print("yes he is in the list")
    
    
# changing item in the list 

Friends[4] = "gaurav"
print(Friends )