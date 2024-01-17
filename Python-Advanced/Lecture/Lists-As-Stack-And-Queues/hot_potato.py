from collections import deque


kids = deque(input().split())
hot_toss = int(input())

while len(kids) > 1:
    kids.rotate(-(hot_toss-1))

    print(f'Removed {kids.popleft()}')

print(f"Last is {kids.popleft()}")

