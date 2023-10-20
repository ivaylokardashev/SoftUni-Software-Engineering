def is_indexes_incorrect(first_index, second_index, memory_game_list):
    return (first_index == second_index or
            first_index < 0 or
            second_index < 0 or
            first_index >= len(memory_game_list) or
            second_index >= len(memory_game_list))


memory_game_list = input().split()
number_of_moves = 0
win_game = 0

while True:
    command = input()
    number_of_moves += 1

    if command == "end":
        print(f"Sorry you lose :(\n{' '.join(memory_game_list)}")
        break

    indexes = sorted(command.split())
    first_index = int(indexes[0])
    second_index = int(indexes[1])

    if is_indexes_incorrect(first_index, second_index, memory_game_list):
        middle_index = len(memory_game_list) // 2
        memory_game_list.insert(middle_index, f"-{number_of_moves}a")
        memory_game_list.insert(middle_index, f"-{number_of_moves}a")
        print("Invalid input! Adding additional elements to the board")

    elif memory_game_list[first_index] == memory_game_list[second_index]:
        # da opitam s tova neshto dolu che mi e interesno
        # memory_game_list.remove(memory_game_list.pop(memory_game_list[first_index]))
        print(f"Congrats! You have found matching elements - {memory_game_list[first_index]}!")
        index_of_removed_elements = memory_game_list.index(memory_game_list[first_index])
        memory_game_list.remove(memory_game_list[first_index])
        memory_game_list.insert(index_of_removed_elements, ' ')
        index_of_removed_elements = memory_game_list.index(memory_game_list[second_index])
        memory_game_list.remove(memory_game_list[second_index])
        memory_game_list.insert(index_of_removed_elements, ' ')
        memory_game_list.remove(' ')
        memory_game_list.remove(' ')

    elif memory_game_list[first_index] != memory_game_list[second_index]:
        print("\Try again!")

    if len(memory_game_list) == 0:
        print(f"You have won in {number_of_moves} turns!")
        break

