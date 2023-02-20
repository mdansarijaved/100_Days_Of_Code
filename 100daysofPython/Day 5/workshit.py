# program to demonstrate the use of functions and passing the different types of arguments to functions
# doing palindrome question using functions;

def palindrome(text): 
    length = int( len(text))
    count = 0 
    for i in range(length): 
        if text[i] == text[-i-1]:
            count = count +1
        
    if count == length:
        print("yes it is palindrome")
    else:
            print("not palindrome")
            

term = input("Enter your string or number : ")
palindrome(term)