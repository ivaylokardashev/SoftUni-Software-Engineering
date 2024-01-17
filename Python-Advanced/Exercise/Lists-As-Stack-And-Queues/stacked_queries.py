stack = []

map_functions = {
    "1": lambda x: stack.append(x[1]),
    "2": lambda x: stack.pop() if stack else None,
    "3": lambda x: print(max(stack)) if stack else None,
    "4": lambda x: print(min(stack)) if stack else None,
}


for _ in range(int(input())):
    data = input().split()
    command = data[0]
    map_functions[command](data)

stack.reverse()

print(*stack, sep=', ')

