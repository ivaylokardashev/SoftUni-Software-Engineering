animals = {}
areas = {}
while True:
    command = input().split(': ')

    if command[0] == 'EndDay':
        break
    if command[0] == 'Add':
        animal_name, needed_food_quantity, area = command[1].split('-')
        if animal_name not in animals:
            animals[f'{animal_name}'] = [int(needed_food_quantity), area]
            if area not in areas:
                areas[f'{area}'] = 1
            else:
                areas[area] += 1
        else:
            animals[animal_name][0] += int(needed_food_quantity)




    elif command[0] == 'Feed':
        animal_name, food = command[1].split('-')
        if animal_name in animals:
            animals[animal_name][0] -= int(food)
            if animals[animal_name][0] <= 0:
                if animals[animal_name][1] in areas:
                    areas[animals[animal_name][1]] -= 1
                    if areas[animals[animal_name][1]] == 0:
                        areas.pop(animals[animal_name][1])
                animals.pop(animal_name)
                print(f"{animal_name} was successfully fed")

print("Animals:")
for key, value in animals.items():
    print(f"{key} -> {value[0]}g")
print("Areas with hungry animals:")
for key, value in areas.items():
    print(f"{key}: {value}")
