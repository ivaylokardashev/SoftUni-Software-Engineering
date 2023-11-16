courses = {}

while True:
    command = input().split(" : ")

    if command[0] == "end":
        break

    course_name = command[0]
    student_name = command[1]

    if course_name not in courses:
        courses[f"{course_name}"] = []

    courses[f"{course_name}"].append(student_name)

for (key, value) in courses.items():
    print(f"{key}: {len(value)}\n-- ", end='')
    print("\n-- ".join(value))