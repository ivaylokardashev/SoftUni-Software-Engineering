# from collections import deque
#
#
# color_string = deque(input().split())
#
# form_secondary_colors = {
#     "orange": lambda color_list: True if {"red", "yellow"}.issubset(color_list) else False,
#     "purple": lambda color_list: True if {"red", "blue"}.issubset(color_string) else False,
#     "green": lambda color_list: True if {"yellow", "blue"}.issubset(color_string) else False,
# }
#
# color_container = list()
#
# while color_string:
#
##############################################################################
# TODO: Understand this code how it's work and what kind of knoledge can I use
##############################################################################
from collections import deque


words = deque(input().split())

colors = {"red", "yellow", "blue", "purple", "orange", "green"}
req_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"blue", "yellow"},
}

result = []

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ''

    for color in (first_word + second_word, second_word + first_word):
        if color in colors:
            result.append(color)
            break
    else:
        for el in (first_word[:-1], second_word[:-1]):
            if el:
                words.insert(len(words) // 2, el)

for color in set(req_colors.keys()).intersection(result):
    if not req_colors[color].issubset(result):
        result.remove(color)

print(result)