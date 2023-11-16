substring = input()
my_string = input()

while substring in my_string:
    my_string = my_string.split(substring)
    my_string = ''.join(my_string)

print(my_string)
