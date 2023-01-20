fruit = ["apple", "banana", "cherry"]
i = 0
for i in range(len(fruit)):
    if fruit[i] == "banana":
        continue
    print(fruit[i])
    
    i+=1