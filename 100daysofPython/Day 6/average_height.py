student_height = input("Enter the student heights: ").split()
for n in range(0,len(student_height)):
    student_height[n]=int(student_height[n])
print(student_height)
# total=sum(student_height)
total = 0
num_students = 0
for i in student_height:
    num_students+=1;
# print(num_students)
for i in range(0,len(student_height)):
    total = total + student_height[i]
print(total)


average = total/num_students
print(average)
    