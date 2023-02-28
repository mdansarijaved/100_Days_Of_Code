t = int(input())
while t > 0: 
    x ,y = map(int,input().split())
    inputA = [0]*x
    inputA = map(int,input().split())
    print(inputA)

    # for i in inputA: 
    #     # print(inputA[i])
    #     if inputA[i]<= y: 
    #         print("1")
    #         y = y - inputA[i]
    #     else: 
    #         print("0")
    t -=1