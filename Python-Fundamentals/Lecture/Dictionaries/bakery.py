items_to_unpacked = input().split()
food = items_to_unpacked[::2]
quantities = items_to_unpacked[1::2]
table_of_stock = {f: q for (f, q) in zip(food, quantities)}

print(table_of_stock)
