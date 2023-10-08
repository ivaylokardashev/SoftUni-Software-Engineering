number_of_lines = int(input())
tank_capacity = 255
water_fueled = 0

for line in range(number_of_lines):
    water = int(input())

    if tank_capacity < water:
        print(f"Insufficient capacity!")
        continue

    tank_capacity -= water
    water_fueled += water

print(water_fueled)