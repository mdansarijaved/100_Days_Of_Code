# cook your dish here
t = int(input())
while t > 0: 
    x,y,z,a = map(int,input().split())
    t1 = z/x
    t2 = a/y
    total = t1+t2
    print(int(total))
    t-=1