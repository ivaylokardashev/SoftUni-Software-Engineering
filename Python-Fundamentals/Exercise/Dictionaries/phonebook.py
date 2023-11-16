phone_book = {}

while True:
    command = input().split('-')
    if command[0].isnumeric():
        break
    name = command[0]
    phone_number = command[1]
    if name not in phone_book.keys():
        phone_book[f"{name}"] = phone_number

n = int(command[0])

for search_contact in range(n):
    name = input()
    if name in phone_book:
        print(f"{name} -> {phone_book[name]}")
    else:
        print(f"Contact {name} does not exist.")
