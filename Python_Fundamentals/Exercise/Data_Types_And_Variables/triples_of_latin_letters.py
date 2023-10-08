number_of_characters = int(input())

for first_char in range(0, number_of_characters):
    for second_char in range(0, number_of_characters):
        for third_char in range(0, number_of_characters):
            print(f"{chr(97 + first_char)}{chr(97 + second_char)}{chr(97 + third_char)}")