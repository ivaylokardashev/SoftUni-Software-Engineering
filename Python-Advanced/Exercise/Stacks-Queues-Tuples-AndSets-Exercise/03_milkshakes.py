from collections import deque


chocolates = list(map(int, input().split(', ')))
cup_of_milk = deque(map(int, input().split(', ')))

count_of_milk_shake = 0

while True:
    if not chocolates or not cup_of_milk or count_of_milk_shake == 5:
        break

    last_chocolate = chocolates.pop()
    first_cup_of_milk = cup_of_milk.popleft()

    if last_chocolate <= 0:
        if first_cup_of_milk > 0:
            cup_of_milk.appendleft(first_cup_of_milk)
        continue

    elif first_cup_of_milk <= 0:
        if last_chocolate > 0:
            chocolates.append(last_chocolate)
        continue

    if not first_cup_of_milk == last_chocolate:
        cup_of_milk.append(first_cup_of_milk)
        chocolates.append(last_chocolate - 5)
        continue

    count_of_milk_shake += 1

if count_of_milk_shake >= 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: ", end='')
    print(*chocolates, sep=', ')
else:
    print("Chocolate: empty")

if cup_of_milk:
    cups_unpacked = [*cup_of_milk]
    print(f"Milk: ", end='')
    print(*cups_unpacked, sep=', ')
else:
    print("Milk: empty")
