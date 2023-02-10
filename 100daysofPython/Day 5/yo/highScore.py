student_score = input("Enter the students Marks: ").split()
for i in range(0,len(student_score)):
    student_score[i] = int(student_score[i])
print(student_score)
highest = 0
for i in student_score:
    if i > highest:
        highest = i
    else:
        highest = highest
print(f"The number is class is {highest}")

j = 0

for i in range(1,101):
    j+=i
print(j)
        
    
    
    