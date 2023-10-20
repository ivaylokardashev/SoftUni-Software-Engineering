total_price_without_taxes = 0
total_taxes = 0
total_price = 0

while True:
    command = input()

    if command == "special":
        total_price = (total_price_without_taxes + total_taxes) - (total_price_without_taxes + total_taxes) * 0.10
        break

    elif command == "regular":
        total_price = total_price_without_taxes + total_taxes
        break

    price_for_part = float(command)

    if price_for_part <= 0:
        print(f"Invalid price!")
        continue

    total_price_without_taxes += price_for_part
    total_taxes += price_for_part * 0.20

if total_price_without_taxes == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price_without_taxes:.2f}$\n"
          f"Taxes: {total_taxes:.2f}$\n"
          "-----------\n"
          f"Total price: {total_price:.2f}$")
