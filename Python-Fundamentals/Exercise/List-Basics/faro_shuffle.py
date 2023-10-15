faro_shuffle = input().split(" ")
shuffles = int(input())

for current_shuffle in range(shuffles):
    first_half = faro_shuffle[:len(faro_shuffle) // 2]
    second_half = faro_shuffle[len(faro_shuffle) // 2:]
    faro_shuffle = []

    for current_card_turn in range(len(first_half)):
        faro_shuffle.append(first_half[current_card_turn])
        faro_shuffle.append(second_half[current_card_turn])


print(faro_shuffle)
