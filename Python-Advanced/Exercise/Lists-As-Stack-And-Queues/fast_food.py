from collections import deque


food = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

for _ in range(len(orders)):
    if food >= orders[0]:
        food -= orders.popleft()
    else:
        print(f'Orders left: {" ".join([str(x) for x in orders])}')
        break
else:
    print('Orders complete')

