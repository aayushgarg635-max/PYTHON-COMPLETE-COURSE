# A list of tuples containing Student Names and grades
student_grades = [("Aryan", 85),("mayank", 92),("rohan", 78),("mohan", 95)]

# 1 Adding a new student to the list
new_student = ("sohan", 88)
student_grades.append(new_student)

# 2. Print all students and their grades
print("Student Records:")
for student, grade in student_grades:
    print(f"- {student}: {grade}")

# 3. Calculate the average grade
total_points = 0
for student, grade in student_grades:
    total_points += grade

average_grade = total_points / len(student_grades)
print(f"\nAverage Class Grade: {average_grade:2f}")

# this is a python program showing grades of students and overall average of whole class
