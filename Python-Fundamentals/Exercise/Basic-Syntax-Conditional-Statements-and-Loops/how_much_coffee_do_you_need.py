list_with_commands = ["coding", "dog", "cat", "movie"]
coffees = 0
while True:
    command = input()
    if command == "END":
        break
    elif command.lower() in list_with_commands:
        if command.isupper():
            coffees += 2
        else:
            coffees += 1
if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)