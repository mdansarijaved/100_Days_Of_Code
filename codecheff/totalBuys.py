# cook your dish here
num = int(input())
while num > 0: 
    tens , fives , cost = map(int, input().split())
    totalMoney = (tens*10) + (fives*5)
    totalBuys = int(totalMoney/cost)
    print(totalBuys)
    num = num -1
