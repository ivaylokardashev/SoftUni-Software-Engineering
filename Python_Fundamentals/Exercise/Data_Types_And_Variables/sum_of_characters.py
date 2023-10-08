number_of_characters = int(input())
total_sum = 0

for char in range(number_of_characters):
    current_char = input()
    total_sum += ord(current_char)

print(f"{total_sum}")