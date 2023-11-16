n = int(input())
good_grade_students = {}

for index in range(n):
    student_name = input()
    student_grade = float(input())

    if student_name not in good_grade_students:
        good_grade_students[f"{student_name}"] = []

    good_grade_students[f"{student_name}"].append(student_grade)

for (key, value) in good_grade_students.items():
    average_grade = sum(value) / len(value)
    if average_grade >= 4.5:
        print(f"{key} -> {average_grade:.2f}")

