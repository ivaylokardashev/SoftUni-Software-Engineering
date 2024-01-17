password = input()

while True:
    command = input().split()
    decision = command[0]
    if decision == "Complete":
        break
    elif decision == "Make":
        deistvie = command[1]
        index_of_char = int(command[2])
        if deistvie == "Upper":
            password_list = list(password)
            char = password_list[index_of_char]
            password_list.pop(index_of_char)
            password_list.insert(index_of_char, char.upper())
            password = ''.join(password_list)
            print(password)
        elif deistvie == "Lower":
            password_list = list(password)
            char = password_list[index_of_char]
            password_list.pop(index_of_char)
            password_list.insert(index_of_char, char.lower())
            password = ''.join(password_list)
            print(password)
    elif decision == "Insert":
        index = int(command[1])
        if 0 <= index < len(password):
            password_list = list(password)
            password_list.insert(index, command[2])
            password = ''.join(password_list)
            print(password)
    elif decision == "Replace":
        get_ascii = (int(ord(command[1])) + int(command[2]))
        if command[1] in password:
            password = password.replace(command[1], chr(get_ascii))
            print(password)
    elif decision == "Validation":
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        incorect_characters = False
        upper_case_letter = False
        lower_case_letter = False
        digit_case = False
        for character in password:
            if character.isupper():
                upper_case_letter = True
            elif character.islower():
                lower_case_letter = True
            elif character.isdigit():
                digit_case = True
            elif character != '_':
                incorect_characters = True

        if incorect_characters:
            print("Password must consist only of letters, digits and _!")
        if not upper_case_letter:
            print("Password must consist at least one uppercase letter!")
        if not lower_case_letter:
            print("Password must consist at least one lowercase letter!")
        if not digit_case:
            print("Password must consist at least one digit!")