# import os
#
# # # path of the current script
# # path = 'D:/Pycharm projects/gfg'
#
# # Before creating
# dir_list = os.listdir()
# print("List of directories and files before creation:")
# print(dir_list)
# print()
#
# file_name = ""
#
# while file_name != "end":
#     file_name = input()
#     # Creates a new file
#     with open(f'{file_name}.py', 'w') as fp:
#         pass
#
# # After creating
# dir_list = os.listdir()
# print("List of directories and files after creation:")
# print(dir_list)

if 'Name: Chi, Age: 2, Gender: Female\n' != 'Name: Chi, Age: 2, Gender: Female':
    print("Yes\n")

a = [1,2,3]
lw = "\n".join(str(el) for el in a)
print(lw)