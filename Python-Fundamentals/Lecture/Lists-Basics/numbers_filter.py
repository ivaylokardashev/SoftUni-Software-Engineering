n_loops = int(input())
list_with_numbers = []
filtered_list_by_command = []
for current_loop in range(n_loops):
    number = int(input())
    list_with_numbers.append(number)
command = input()
for current_element in list_with_numbers:
    if command == "even":
        if current_element % 2 == 0:
            filtered_list_by_command.append(current_element)
    elif command == "odd":
        if current_element % 2 != 0:
            filtered_list_by_command.append(current_element)
    elif command == "negative":
        if current_element < 0:
            filtered_list_by_command.append(current_element)
    elif command == "positive":
        if current_element >= 0:
            filtered_list_by_command.append(current_element)
print(filtered_list_by_command)