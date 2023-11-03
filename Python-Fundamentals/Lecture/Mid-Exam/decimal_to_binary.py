number = int(input())
binary = []
wrong_number = False

for weigh in range(7, -1, -1):
    if number > 255 or number < 0:
        print("Wrong number you can't enter number less than 0 and greater than 255!")
        wrong_number = True
        break

    if number >= 2 ** weigh:
        number = number - 2 ** weigh
        binary.append(1)
    else:
        binary.append(0)

if not wrong_number:
    print(binary)

#new
    # if tourist - 4 >= 0:
    #     if total_space_in_wagons[current_wagons] == 0:
    #         tourist -= 4
    #         total_space_in_wagons[current_wagons] += 4
    #     else:
    #         tourist -= 4 - total_space_in_wagons[current_wagons]
    #         total_space_in_wagons[current_wagons] += 4 - total_space_in_wagons[current_wagons]
    # else:
    #     if total_space_in_wagons[current_wagons] == 0:
    #         total_space_in_wagons[current_wagons] += tourist
    #         tourist = 0
    #     else:
    #         tourist -= 4 - total_space_in_wagons[current_wagons]
    #         total_space_in_wagons[current_wagons] += 4 - total_space_in_wagons[current_wagons]