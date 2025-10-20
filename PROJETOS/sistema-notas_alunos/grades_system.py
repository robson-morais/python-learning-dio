import grades_bib

student_count = 1
students_list = []

for i in range(0, student_count, 1):

    # Student registration in the system:
    student_data = []
    student_grades = []
    
    name = input("Name: ")
    student_data.append(name)
    student_data.append(student_grades)

    grade1 = float(input("Grade 1: "))
    grade2 = float(input("Grade 2: "))
    grade3 = float(input("Grade 3: "))
    student_grades.append(grade1)
    student_grades.append(grade2)
    student_grades.append(grade3)

    students_list.append(student_data)

    # Analysis of the student's grades:
    student_average = grades_bib.calculate_average(student_grades)
    student_result = grades_bib.result(student_average)

    print(f"""
    ======
    Name: {name}
    Grades: {student_grades}
    Average: {student_average: .2f}
    Result: {student_result}
    ======
""")