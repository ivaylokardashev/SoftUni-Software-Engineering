sequence = input()
previous = ""

for char in sequence:
    if char != previous:
        print(f"{char}", end='')

    previous = char
