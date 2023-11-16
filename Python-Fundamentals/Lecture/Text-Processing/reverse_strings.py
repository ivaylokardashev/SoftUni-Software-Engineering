strings_and_reversed_strings = {}

while True:
    command = input()

    if command == "end":
        break

    strings_and_reversed_strings[f"{command}"] = command[::-1]

for (key, value) in strings_and_reversed_strings.items():
    print(f"{key} = {value}")
