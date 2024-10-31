students = []
avg = 0

n = int(input())
for i in range(n):
    student = {}

    student["name"], *student["grades"] = input().split()
    student["grades"] = list(map(float, student["grades"]))

    students.append(student)

selected_student = input()

for student in students:
    if student["name"] == selected_student:
        avg = sum(student["grades"]) / len(student["grades"])    

print(f"{avg:.2f}")