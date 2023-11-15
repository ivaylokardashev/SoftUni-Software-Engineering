items_to_unpacked = input().split()
products_to_search = input().split()

food = items_to_unpacked[::2]
quantities = items_to_unpacked[1::2]
table_of_stock = {f: int(q) for (f, q) in zip(food, quantities)}

for product in products_to_search:
    if product in table_of_stock.keys():
        if table_of_stock[product] > 0:
            print(f"We have {table_of_stock[product]} of {product} left")
            continue

    print(f"Sorry, we don't have {product}")
