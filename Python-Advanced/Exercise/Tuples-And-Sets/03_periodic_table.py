unique_elements = set()

for _ in range(int(input())):
    elements = input().split()
    unique_elements.update(*[elements])

print(*unique_elements, sep='\n')