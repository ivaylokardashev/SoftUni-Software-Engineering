table_of_products = {}

while True:
    command = input().split(': ')

    if command[0] == "statistics":
        break

    key, value = command[0], command[1]

    if key not in table_of_products.keys():
        table_of_products[f'{key}'] = int(value)
        continue

    table_of_products[f'{key}'] += int(value)

print("Products in stock:")
for key, value in table_of_products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(table_of_products)}")
print(f"Total Quantity: {sum(table_of_products.values())}")
