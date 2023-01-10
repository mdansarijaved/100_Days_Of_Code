import random

Friends = ["anne", "beckyy", "sam"]
# A list can have elements of different data types

rannum = random.randint(0, 2)

print(Friends[rannum])

print(Friends[-1])

Friends.append("james")
# Append adds an element to the end of the list

print(Friends)

Friends.insert(3, "afzal")
#insert adds an element at a specific index

print(Friends)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))
# count counts the number of times an element appears in a list

print(fruits.count('tangerine'))

print(fruits.index('banana'))
#index returns the index of the first element that matches the argument

print(fruits.index('banana', 4))  # Find next banana starting at position 4

fruits.reverse()
#reverse reverses the order of the elements in the list


print(fruits)


fruits.append('grape')


print(fruits)


fruits.sort()
#sort sorts the elements of the list

print(fruits)

fruits.pop()
#pop removes the last element of the list
