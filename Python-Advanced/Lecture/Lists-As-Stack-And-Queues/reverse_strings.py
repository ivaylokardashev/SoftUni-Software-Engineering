sentence = list(input())

for _ in sentence.copy():
    print(f"{sentence.pop()}", end='')
