# cook your dish here

num = int(input())
while num > 0: 
    num1 , num2 = map(int, input().split())
    maxnum = max(num1 , num2 )
    print(maxnum)
    num = num -1
    
    