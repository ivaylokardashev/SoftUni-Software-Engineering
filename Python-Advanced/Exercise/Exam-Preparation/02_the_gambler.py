def print_board(board):
    for row in board:
        print(''.join(row))


def get_symbol(matrix, current_position):
    symbol = matrix[current_position[0]][current_position[1]]
    return symbol


# def movement(matrix, current_position)

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

size_of_matrix = int(input())
matrix = list()
current_position = list()
total_amount = 100

for row in range(size_of_matrix):
    sequence = [c for c in input()]
    matrix.append([sequence[col] if sequence[col] != 'G' else current_position.extend([row, col])
                   for col in range(len(sequence))])

matrix[current_position[0]][current_position[1]] = '-'

command = input()

while command != "end":
    try:
        row_aproach = current_position[0] + moves.get(command)[0]
        col_aproach = current_position[1] + moves.get(command)[1]

        if not (0 <= row_aproach < size_of_matrix and 0 <= col_aproach < size_of_matrix):
            raise IndexError
    except TypeError:
        command = input()
        continue
    except IndexError:
        print(f"Game over! You lost everything!")
        exit()

    matrix[current_position[0]][current_position[1]] = '-'
    current_position[0], current_position[1] = row_aproach, col_aproach
    symbol = get_symbol(matrix, current_position)
    matrix[current_position[0]][current_position[1]] = 'G'

    if symbol == '-':
        pass
    elif symbol == 'W':
        total_amount += 100
    elif symbol == 'P':
        total_amount -= 200
        if total_amount <= 0:
            print(f"Game over! You lost everything!")
            break
    elif symbol == 'J':
        total_amount += 100000
        print(f"You win the Jackpot!\nEnd of the game. Total amount: {total_amount}$")
        print_board(matrix)
        exit()

    command = input()
else:
    print(f"End of the game. Total amount: {total_amount}$")
    print_board(matrix)
    exit()
