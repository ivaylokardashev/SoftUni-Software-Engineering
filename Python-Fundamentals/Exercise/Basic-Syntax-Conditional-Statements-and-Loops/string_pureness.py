number_of_strings = int(input())
not_pure_signs = (',', '.', '_')
current_string = "."
result = current_string.find(str(map(lambda c: [i for i in not_pure_signs], not_pure_signs)))
print(result)
# for i in range(number_of_strings):
#     current_string = input()
#     if bool(map(lambda c: True if current_string.find(c) else False, not_pure_signs)):
#         print(f"{current_string} is not pure.")
#     else:
#         print(f"{current_string} is pure.")



# number_of_strings = int(input())
# for i in range(number_of_strings):
#     current_string = input()
#     if ',' in current_string or '.' in current_string or '_' in current_string:
#         print(f"{current_string} is not pure!")
#     else:
#         print(f"{current_string} is pure.")