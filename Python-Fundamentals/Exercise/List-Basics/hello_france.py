TRAIN_TICKET_FRANCE = 150
MAXIMUM_CLOTHES_PRICE = 50.00
MAXIMUM_SHOES_PRICE = 35.00
MAXIMUM_ACCESSORIES_PRICE = 20.50
MARKUP = 40 / 100


def get_only_type_and_price(items):
    temp = ' '.join(items)
    items = temp.split('->')
    temp = ' '.join(items)
    items = temp.split(' ')

    return items


def get_markup(price_for_item):
    price_with_markup = price_for_item * MARKUP + price_of_item

    return price_with_markup


items = input().split('|')
budget = float(input())

items = get_only_type_and_price(items)
bought_items_with_new_price = []
old_budget = budget


for current_item in range(0, len(items) - 1, 2):
    item = items[current_item]
    price_of_item = float(items[current_item + 1])

    if item == "Clothes":
        if price_of_item <= MAXIMUM_CLOTHES_PRICE and budget - price_of_item >= 0:
            budget -= price_of_item
            bought_items_with_new_price.append(get_markup(price_of_item))

    elif item == "Shoes":
        if price_of_item <= MAXIMUM_SHOES_PRICE and budget - price_of_item >= 0:
            budget -= price_of_item
            bought_items_with_new_price.append(get_markup(price_of_item))

    elif item == "Accessories":
        if price_of_item <= MAXIMUM_ACCESSORIES_PRICE and budget - price_of_item >= 0:
            budget -= price_of_item
            bought_items_with_new_price.append(get_markup(price_of_item))


for element in range(len(bought_items_with_new_price)):
    print(f"{bought_items_with_new_price[element]:.2f}", end=' ')


profit = budget + sum(bought_items_with_new_price) - old_budget

print(f"\nProfit: {profit:.2f}")

if profit + old_budget >= TRAIN_TICKET_FRANCE:
    print("Hello, France!")

else:
    print("Not enough money.")
