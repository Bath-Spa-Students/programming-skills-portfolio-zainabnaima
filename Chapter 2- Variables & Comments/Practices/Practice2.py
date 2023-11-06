'''Q2: Write a python program that takes courses marks as input and then calculates
 average of all the courses. After calculating the average, calculate the percentage
 of a student using total marks. Assume the total of all the courses marks is 500 
 or take the total marks from the user as input. '''

# Input marks 
marks_list = []
total_marks = 0

num_courses = int(input("Enter the number of courses: "))

for i in range(num_courses):
    marks = int(input(f"Enter marks for course {i + 1}: "))
    marks_list.append(marks)
    total_marks += marks

average = total_marks / num_courses

# Assuming total marks is 500
total_marks_input = 500
percentage = (total_marks / total_marks_input) * 100

print(f"Average marks: {average}")
print(f"Percentage: {percentage}%")
