name_of_gifts = input().split()

while True:
    command = input().split()

    if command[0] == "No":
        break

    elif command[0] == "OutOfStock":
        for find_element in range(len(name_of_gifts)):
            if name_of_gifts[find_element] == command[1]:
                name_of_gifts[find_element] = None

    elif command[0] == "Required":
        index = int(command[2])
        parameter = command[1]

        if 0 <= index < len(name_of_gifts):
            name_of_gifts.pop(index)
            name_of_gifts.insert(index, parameter)

        else:
            continue

    elif command[0] == "JustInCase":
        name_of_gifts.pop()
        name_of_gifts.append(command[1])


for current_gift in range(len(name_of_gifts)):
    if name_of_gifts[current_gift] is None:
        continue

    elif current_gift == len(name_of_gifts) - 1:
        print(name_of_gifts[current_gift])

    else:
        print(name_of_gifts[current_gift], end=' ')
