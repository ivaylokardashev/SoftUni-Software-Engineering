def get_only_level_and_cells_of_fire(level_of_fire):
    temp = ' '.join(level_of_fire)
    level_of_fire = temp.split(' = ')
    temp = ' '.join(level_of_fire)
    level_of_fire = temp.split(' ')

    return level_of_fire


level_of_fire = input().split('#')
water = int(input())

level_of_fire = get_only_level_and_cells_of_fire(level_of_fire)

effort = 0
total_fire = 0
valid_cells = []

for element in range(0, len(level_of_fire) - 1, 2):
    type_and_cell = [level_of_fire[element]] + [level_of_fire[element + 1]]

    if type_and_cell[0] == "High":
        if 81 <= int(type_and_cell[1]) <= 125 and water - int(type_and_cell[1]) >= 0:
            water -= int(type_and_cell[1])
            effort += int(type_and_cell[1]) * (25 / 100)
            total_fire += int(type_and_cell[1])

            valid_cells.append(type_and_cell[1])

            continue

    elif type_and_cell[0] == "Medium":
        if 51 <= int(type_and_cell[1]) <= 80 and water - int(type_and_cell[1]) >= 0:
            water -= int(type_and_cell[1])
            effort += int(type_and_cell[1]) * (25 / 100)
            total_fire += int(type_and_cell[1])

            valid_cells.append(type_and_cell[1])

            continue

    elif type_and_cell[0] == "Low":
        if 1 <= int(type_and_cell[1]) <= 50 and water - int(type_and_cell[1]) >= 0:
            water -= int(type_and_cell[1])
            effort += int(type_and_cell[1]) * (25 / 100)
            total_fire += int(type_and_cell[1])

            valid_cells.append(type_and_cell[1])

            continue

print("Cells:")

for cells in range(len(valid_cells)):
    print(f" - {valid_cells[cells]}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

