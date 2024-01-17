encrypted_message = input()

while True:
    command = input().split('|')

    if command[0] == "Decode":
        print(f"The decrypted message is: {encrypted_message}")
        break
    elif command[0] == "Move":
        end_index = int(command[1])
        move_part_front = encrypted_message[:end_index]
        move_part_end = encrypted_message[end_index:]
        move_part_front, move_part_end = move_part_end, move_part_front
        encrypted_message = move_part_front + move_part_end
    elif command[0] == "Insert":
        insert_index = int(command[1])
        insert_element = command[2]
        encrypted_message = encrypted_message[:insert_index] + f'{insert_element}' + encrypted_message[insert_index:]
    elif command[0] == "ChangeAll":
        old_char = command[1]
        new_char = command[2]
        encrypted_message = encrypted_message.replace(old_char, new_char)

