company_employees = {}

while True:
    command = input().split(" -> ")

    if command[0] == "End":
        break

    company = command[0]
    employees_id = command[1]

    if company not in company_employees:
        company_employees[f"{company}"] = []

    if employees_id not in company_employees[f"{company}"]:
        company_employees[f"{company}"].append(employees_id)

for (key, value) in company_employees.items():
    print(f"{key}\n-- ", end='')
    print("\n-- ".join(value))
