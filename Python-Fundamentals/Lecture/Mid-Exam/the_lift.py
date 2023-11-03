tourist = int(input())
total_space_in_wagons = [int(space) for space in input().split()]

for current_wagons in range(len(total_space_in_wagons)):
    if tourist == 0:
        break

    if tourist >= 4:
        if total_space_in_wagons[current_wagons] == 0:
            tourist -= 4
            total_space_in_wagons[current_wagons] += 4

        elif total_space_in_wagons[current_wagons] != 0:
            old_space = total_space_in_wagons[current_wagons]
            tourist -= 4 - total_space_in_wagons[current_wagons]
            total_space_in_wagons[current_wagons] += 4 - total_space_in_wagons[current_wagons]

    elif tourist < 4:
        total_space_in_wagons[current_wagons] += tourist
        tourist -= tourist

if tourist == 0:
    total_space_in_wagons = map(str, total_space_in_wagons)
    print("The lift has empty spots!\n"
          f"{' '.join(total_space_in_wagons)}")
else:
    total_space_in_wagons = map(str, total_space_in_wagons)
    print(f"There isn't enough space! {tourist} people in a queue!\n"
          f"{' '.join(total_space_in_wagons)}")
