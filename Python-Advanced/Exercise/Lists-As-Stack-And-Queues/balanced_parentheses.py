from collections import deque


parentheses = deque([parenthes for parenthes in input()])

balanced = {
    '[': lambda x: True if x == ']' else False,
    '{': lambda x: True if x == '}' else False,
    '(': lambda x: True if x == ')' else False,
}

stack = []
parentheses_copy = parentheses.copy()

for index in range(len(parentheses)-1, -1, -1):
    if parentheses[index] == '(' or parentheses[index] == '[' or parentheses[index] == '{':
        match_flag = balanced[parentheses.pop()](stack.pop())

        if not match_flag:
            print('NO')
            break
    else:
        stack.append(parentheses.pop())
else:
    print('YES')
