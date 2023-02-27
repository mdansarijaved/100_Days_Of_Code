# cook your dish here
num = int(input())
while num > 0:
    x ,y ,p = map(int,input().split())
    total = (x*3) - (x-y)
    if total >= p: 
        print("PASS")
    else: 
        print("Fail")
    num = num - 1