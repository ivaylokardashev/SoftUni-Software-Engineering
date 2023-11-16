force_book = {}

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if "|" in command:
        command = command.split(" | ")
        force_side, force_user = command[0], command[1]
        if force_side not in force_book:
            force_book[f"{force_side}"] = []
            for key, value in force_book.items():
                if force_user in value:
                    command = "This user exist"
                    break
            if command != "This user exist":
                force_book[f"{force_side}"].append(force_user)
        elif force_side in force_book:
            for key, value in force_book.items():
                if force_user in value:
                    command = "This user exist"
                    break
            if command != "This user exist":
                force_book[f"{force_side}"].append(force_user)
    else:
        command = command.split(" -> ")
        force_side, force_user = command[1], command[0]

        for key, value in force_book.items():
            if force_user in value:
                command = "This user exist"
                break

        if command == "This user exist":
            for key, value in force_book.items():
                if force_user in value:
                    user_index = value.index(force_user)
                    value.pop(user_index)
                    if force_side not in force_book:
                        force_book[f"{force_side}"] = []
                    force_book[f"{force_side}"].append(force_user)
                    break
        elif command != "This user exist":
            if force_side not in force_book:
                force_book[f"{force_side}"] = []
            force_book[f"{force_side}"].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

for key, value in force_book.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}\n! ", end='')
        print("\n! ".join(value))


