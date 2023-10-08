num = int(input())

for i in range(2, int(num / 2) + 1):
    if num % i == 0:
        print(False)
        break
else:
    print(True)
