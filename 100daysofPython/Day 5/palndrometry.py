string = input()
s = list(string)
s.reverse()
si = "".join(s)
if((si)==(string)):
    print("Palindroe")
else:
    print("Not Palindrome")