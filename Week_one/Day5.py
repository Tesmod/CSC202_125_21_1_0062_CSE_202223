#Day 5 - Loops, Range and Code Block
#Day 5.1 Exercise - Average Height Exercise
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
print("The watermelon is outside the for loop")

#Day 5.1 Average Height Exercise
student_heights = input("Input the list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0 
for height in student_heights:
    total_height += height
print(total_height)

num_of_students = 0
for student in student_heights:
    num_of_students += 1
print(num_of_students)

average_height = round(total_height / num_of_students)
print(average_height)

