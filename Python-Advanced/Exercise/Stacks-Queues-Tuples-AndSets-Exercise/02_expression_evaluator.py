from math import floor


math_list = input().split()

solution = []

while math_list.copy():
    element = math_list.pop()

    if element.isdigit() or len(element) >= 2:
        solution.append(int(element))


# for current_sign in math_list:
#
#     if current_sign.isdigit() or len(current_sign) >= 2:
#         solution.append(int(current_sign))
#
#     elif current_sign == '*':
#         mul = 1
#
#         for element in solution:
#             mul *= element
#         solution = [mul]
#
#     elif current_sign == '+':
#         solution = [sum(solution)]
#
#     elif current_sign == '-':
#         reducible = solution[0]
#
#         for index in range(1, len(solution), 1):
#             reducible -= solution[index]
#
#         solution = [floor(reducible)]
#
#     elif current_sign == '/':
#         divisor = solution[0]
#
#         for index in range(1, len(solution), 1):
#             if solution[index] != 0:
#                 divisor /= solution[index]
#
#         solution = [floor(divisor)]

print(*solution)