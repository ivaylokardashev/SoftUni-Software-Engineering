key = int(input())
n = int(input())

for _ in range(n):
    letter = input()
    print(chr(ord(letter) + key), end="")
