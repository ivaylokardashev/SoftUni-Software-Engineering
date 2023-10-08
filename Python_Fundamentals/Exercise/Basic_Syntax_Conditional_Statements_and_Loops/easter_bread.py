# budget = float(input())
# price_for_kg_floor = float(input())
# price_for_pack_of_eggs = (price_for_kg_floor * (75 / 100))
# price_for_milk = (price_for_kg_floor + price_for_kg_floor * (25 / 100))
# number_of_loaves = 0
# count_for_letter_milk = 0
# colored_eggs_count = 0
# while True:
#     if budget < price_for_kg_floor + price_for_pack_of_eggs + price_for_milk or budget == 2.45:
#         break
#     if number_of_loaves == 0:
#         budget -= price_for_milk + price_for_kg_floor + price_for_pack_of_eggs
#         count_for_letter_milk += 1
#         number_of_loaves += 1
#     else:
#         budget -= price_for_kg_floor + price_for_pack_of_eggs
#         count_for_letter_milk += 1
#         if count_for_letter_milk == 4:
#             budget -= price_for_milk
#             count_for_letter_milk = 0
#         number_of_loaves += 1
#     if number_of_loaves % 3 == 0:
#         colored_eggs_count += 3
#         colored_eggs_count -= number_of_loaves - 2
#     else:
#         colored_eggs_count += 3
#
# print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")
#
budget = float(input())
price_per_kg_flour = float(input())

price_for_pack_eggs = price_per_kg_flour * 0.75
price_for_dose_milk = (price_per_kg_flour * 1.25) / 4

price_per_bread = price_per_kg_flour + price_for_pack_eggs + price_for_dose_milk
leaves_of_bread = 0
eggs = 0

while budget > price_per_bread:

    leaves_of_bread += 1
    eggs += 3
    if leaves_of_bread % 3 == 0:
        eggs -= (leaves_of_bread - 2)
    budget -= price_per_bread

print(f"You made {leaves_of_bread} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")