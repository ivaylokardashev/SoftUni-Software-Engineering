def print_airspace(airspace):
    for row in airspace:
        print(''.join(row))

def get_symbol(airspace, current_position):
    symbol = airspace[current_position[0]][current_position[1]]
    return symbol


moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

protected_airspace = int(input())
airspace = list()
current_position = list()
jetfighter_armor = 300
enemy_count = 4

for row in range(protected_airspace):
    sequence = [c for c in input()]
    airspace.append([sequence[col] if sequence[col] != 'J' else current_position.extend([row, col])
                   for col in range(len(sequence))])

command = input()

while True:
    try:
        row_aproach = current_position[0] + moves.get(command)[0]
        col_aproach = current_position[1] + moves.get(command)[1]

        if not (0 <= row_aproach < protected_airspace and 0 <= col_aproach < protected_airspace):
            raise IndexError
    except TypeError:
        command = input()
        continue
    except IndexError:
        exit()

    airspace[current_position[0]][current_position[1]] = '-'
    current_position[0], current_position[1] = row_aproach, col_aproach
    symbol = get_symbol(airspace, current_position)
    airspace[current_position[0]][current_position[1]] = 'J'

    if symbol == '-':
        pass
    elif symbol == 'E':
        enemy_count -= 1

        if enemy_count == 0:
            print(f"Mission accomplished, you neutralized the aerial threat!")
            print_airspace(airspace)
            break
        else:
            jetfighter_armor -= 100

            if jetfighter_armor == 0:
                x = current_position[1]
                y = current_position[0]
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{y}, {x}]!")
                print_airspace(airspace)
                break
    elif symbol == 'R':
        jetfighter_armor += 300 - jetfighter_armor

    command = input()