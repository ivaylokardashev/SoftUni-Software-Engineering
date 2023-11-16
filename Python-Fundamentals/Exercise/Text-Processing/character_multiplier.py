text = input().split()
longest_str = text[0]
lowest_str = text[1]
sum_of_strings = 0

if len(longest_str) < len(lowest_str):
    longest_str, lowest_str = lowest_str, longest_str

for index in range(len(longest_str)):
    if index <= len(lowest_str) - 1:
        sum_of_strings += ord(longest_str[index]) * ord(lowest_str[index])
        continue

    sum_of_strings += ord(longest_str[index])

print(sum_of_strings)