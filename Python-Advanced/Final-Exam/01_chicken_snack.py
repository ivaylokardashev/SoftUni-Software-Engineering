from collections import deque


amount_of_money = [int(m) for m in input().split()]
price_of_food = deque([int(p) for p in input().split()])

food_count = 0

while len(amount_of_money) != 0 and len(price_of_food) != 0:
    current_money = amount_of_money.pop()
    current_price = price_of_food.popleft()

    if current_money == current_price:
        food_count += 1
        continue
    elif current_money > current_price:
        food_count += 1
        try:
            amount_of_money[-1] += current_money - current_price
        except IndexError:
            continue
    else:
        continue

if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif 0 < food_count < 4:
    if food_count == 1:
        print(f"Henry ate: {food_count} food.")
    else:
        print(f"Henry ate: {food_count} foods.")
elif food_count == 0:
    print(f"Henry remained hungry. He will try next weekend again.")

