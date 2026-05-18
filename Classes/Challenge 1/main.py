from student import Student

student1 = Student("Joan", 18)
student2 = Student("Kristine", 18)
student3 = Student("Leandro", 18)

student_list = [student1, student2, student3]

for student in student_list:
    print(student.greet() + getattr(student,"name") +"!")