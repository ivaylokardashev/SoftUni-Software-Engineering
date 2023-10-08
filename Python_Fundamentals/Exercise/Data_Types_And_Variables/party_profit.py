companions_count = int(input())
days = int(input())
coins = 0

for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        companions_count -= 2

    if current_day % 15 == 0:
        companions_count += 5

    if current_day % 3 == 0:
        coins -= companions_count * 3

    if current_day % 5 == 0:
        coins += companions_count * 20

        if current_day % 3 == 0:
            coins -= companions_count * 2

    coins += 50
    coins -= companions_count * 2

coins = coins // companions_count

print(f"{companions_count} companions received {coins} coins each.")
