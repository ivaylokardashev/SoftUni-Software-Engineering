from collections import deque


bees = deque(map(int, input().split()))
# nectar = list(map(int, input().split()))
nectar = [int(nec) for nec in input().split()]
symbols = deque(input().split())

total_honey = 0

while bees and nectar:
    bee = bees.popleft()
    nec = nectar.pop()

    if bee > nec:
        bees.appendleft(bee)
        continue

    symbol = symbols.popleft()

    if symbol == '/':
        if nec != 0:
           total_honey += abs(bee / nec)
        continue

    total_honey += abs(eval(f"{bee}{symbol}{nec}"))

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join([str(bee) for bee in bees])}")

if nectar:
    print(f"Nectar left: {', '.join([str(nec) for nec in nectar])}")
