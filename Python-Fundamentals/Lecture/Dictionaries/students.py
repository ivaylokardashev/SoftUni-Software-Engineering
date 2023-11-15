students_table = {}
while True:
    students = input().split(':')

    if len(students) > 1:
        key = students[0]
        value = [students[1], students[2]]
        students_table[f"{key}"] = value
    else:
        course = students[0].split('_')
        course = ' '.join(course)
        for key, value in students_table.items():
            if value[1] == course:
                print(f"{key} - {value[0]}")
        break
