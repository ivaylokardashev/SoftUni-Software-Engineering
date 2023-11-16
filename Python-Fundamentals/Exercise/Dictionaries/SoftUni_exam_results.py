exam = {}
languages = {}

while True:
    command = input().split('-')

    if command[0] == "exam finished":
        break

    if command[1] != "banned":
        username, language, points = command[0], command[1], int(command[2])

        if username not in exam:
            exam[f"{username}"] = 0

        if points > exam[f"{username}"]:
            exam[f"{username}"] = points

        if language not in languages:
            languages[f"{language}"] = 0

        languages[f"{language}"] += 1
    else:
        username = command[0]
        exam.pop(username)

print("Results:")
for key, values in exam.items():
    print(f"{key} | {values}")
print("Submissions:")
for key, values in languages.items():
    print(f"{key} - {values}")

