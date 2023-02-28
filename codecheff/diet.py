# cook your dish here
t = int(input())
while t > 0 : 
    ListA = []
    x,y = map(int,input().split())
    for i in range(x):
        a = int(input())
        ListA.append(a)
    print(ListA)
    # count = 0
    # for i in ListA: 
    #     if ListA[i] >= 4: 
    #         ListA[i+1] += ListA[i]-4
    #         count +=1 
    #     else: 
    #         print("NO",ListA[i])
    # if count == x: 
    #     print("YES")
        
    t-=1
            
        