n = int(input())
students = []
students_with_second_lowest_grades = []

for i in range(n):
    students.append([input(), float(input())])

grades = sorted([grade for name, grade in students])
min_grade = grades[0]

second_min_grade = next(grade for grade in grades if grade > min_grade)

students_with_second_lowest_grades = sorted([name for name, grade in students if grade == second_min_grade])
[print(student) for student in students_with_second_lowest_grades]