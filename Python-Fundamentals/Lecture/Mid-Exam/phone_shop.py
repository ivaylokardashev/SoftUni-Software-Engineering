import re


phone_list = input().split(", ")

while True:
    command = input().split(" - ")

    if command[0] == "End":
        break

    if command[0] == "Add":
        phone = command[1]
        if phone not in phone_list:
            phone_list.append(phone)

    elif command[0] == "Remove":
        phone = command[1]
        if phone in phone_list:
            phone_list.remove(phone)

    elif command[0] == "Bonus phone":
        convert_command_to_string = ' '.join(command)
        convert_command_to_list = re.split(' - |:| ', convert_command_to_string)

        old_phone = convert_command_to_list[2]
        new_phone = convert_command_to_list[3]

        if old_phone in phone_list:
            index_of_new_phone = phone_list.index(old_phone) + 1
            phone_list.insert(index_of_new_phone, new_phone)

    elif command[0] == "Last":
        phone = command[1]
        if phone in phone_list:
            phone_list.remove(phone)
            phone_list.append(phone)

print(", ".join(phone_list))
