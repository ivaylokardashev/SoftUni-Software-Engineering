budget = int(input())
costs = 0

while True:
    command = input()

    if command == "End":
        print(f"You bought everything needed.")
        break

    costs += int(command)

    if costs > budget:
        print(f"You went in overdraft!")
        break