expression = list(input())
parentheses_indexes = []

for current_index in range(len(expression)):
    if expression[current_index] == '(':
        parentheses_indexes.append(current_index)
    elif expression[current_index] == ')':
        start = parentheses_indexes.pop()
        end = current_index + 1
        print(''.join(expression[start:end]))

