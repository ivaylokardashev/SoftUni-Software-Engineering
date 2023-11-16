products = {}

while True:
    product = input().split()

    if product[0] == "buy":
        break

    name_of_product = product[0]
    price = float(product[1])
    quantity = int(product[2])

    if name_of_product not in products:
        products[f"{name_of_product}"] = [price, quantity]
    elif name_of_product in products:
        products[f"{name_of_product}"][0] = price
        products[f"{name_of_product}"][1] += quantity

for (key, value) in products.items():
    print(f"{key} -> {(value[0] * value[1]):.2f}")
