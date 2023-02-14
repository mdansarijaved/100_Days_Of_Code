term = input("Enter your string : ")
term = term.lower()
# print(term)
length = int(len(term)/2)
count = 0 

for i in range(length): 
    if term[i] == term[-i-1]:
        count = count +1
    else:
        print("not palindrome")
if count == length:
    print("yes it is palindrome")