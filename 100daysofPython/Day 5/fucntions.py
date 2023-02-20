# # pass by reference means that if you change what a parameter refers to within a function, the change also reflects back in the calling function.
# #pass by value means that if you change a parameter within a function, the change doesn't reflect back in the calling function.

# #pass by refernce ; 
# def add_student(list):
#     list.append(50)
#     print(list)
# my_list = [1,2,3,4,5]
# add_student(my_list)
# print(my_list)


# # pass by value 
# def add_value(a):
#     a = a+10
#     print(a)
# my_value = 10
# add_value(my_value)
# print(my_value)

# def mystring(txt):
#     txt.upper()
#     print(txt)
    
# test = "hello"
# mystring(test)
# print(test)


def mylist(list):
    list[3] = 10
    print(list)

list1 = [1,2,3,4,5]
mylist(list1)
print(list1)

mystring = "hello"
def function1(test):
    mystring = "hellow world"
    print(mystring +" "+ test)
    
function1(mystring)

