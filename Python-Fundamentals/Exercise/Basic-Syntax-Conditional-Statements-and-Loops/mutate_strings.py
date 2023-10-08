first_string = input()
second_string = input()
new_string = ""
last_string = first_string
for character_index in range(len(first_string)):
    left_part = second_string[:character_index + 1]
    right_part = first_string[character_index + 1:]
    new_string = left_part + right_part
    if last_string != new_string:
        print(new_string)
        last_string = new_string