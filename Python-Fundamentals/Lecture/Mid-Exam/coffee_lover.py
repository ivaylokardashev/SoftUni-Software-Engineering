def remove_coffees(num_of_coffees, direction, list_of_coffees):
    if len(list_of_coffees) >= num_of_coffees:
        if direction == "first":
            remove_coffees_in_row = 0
            for remove_coffees in range(num_of_coffees):
                list_of_coffees.pop(remove_coffees_in_row)

        elif direction == "last":
            for remove_coffees in range(num_of_coffees):
                list_of_coffees.pop()


def is_index_valid(index, index_list):
    return 0 <= index < len(index_list)


def swap_prefer_coffee(not_prefer_coffee, prefer_coffee, list_of_coffees):
    list_of_coffees[not_prefer_coffee], list_of_coffees[prefer_coffee] =\
        list_of_coffees[prefer_coffee], list_of_coffees[not_prefer_coffee]


def reverse_list(list_to_be_reversed):
    return list_to_be_reversed[::-1]


list_of_coffees = input().split()
commands = int(input())

for current_command in range(commands):
    command = input().split()

    if command[0] == "Include":
        new_coffee = command[1]
        list_of_coffees.append(new_coffee)

    elif command[0] == "Remove":
        direction = command[1]
        num_of_coffees = int(command[2])
        remove_coffees(num_of_coffees, direction, list_of_coffees)

    elif command[0] == "Prefer":
        not_prefer_coffee = int(command[1])
        prefer_coffee = int(command[2])

        if is_index_valid(not_prefer_coffee, list_of_coffees) and is_index_valid(prefer_coffee, list_of_coffees):
            swap_prefer_coffee(not_prefer_coffee, prefer_coffee, list_of_coffees)

    elif command[0] == "Reverse":
        list_of_coffees = reverse_list(list_of_coffees)

print(f"Coffees:\n{' '.join(list_of_coffees)}")
