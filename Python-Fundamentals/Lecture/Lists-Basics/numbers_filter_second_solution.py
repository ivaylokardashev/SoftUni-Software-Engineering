nums = int(input())

COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_POSITIVE = 'positive'
COMMAND_NEGATIVE = 'negative'

number_list = [int(input()) for x in range(nums)]

command = input()
filtered_list = []

for element in number_list:
    filtered_command = ((COMMAND_EVEN == command and element % 2 == 0) or
                        (COMMAND_ODD == command and element % 2 != 0) or
                        (COMMAND_POSITIVE == command and element >= 0) or
                        (COMMAND_NEGATIVE == command and element < 0))

    if filtered_command:
        filtered_list.append(element)

print(filtered_list)
