start_character_sequence = int(input())
end_character_sequence = int(input())

for number in range(start_character_sequence, end_character_sequence + 1):
    if number != end_character_sequence:
        print(chr(number), end=" ")
    else:
        print(chr(number))