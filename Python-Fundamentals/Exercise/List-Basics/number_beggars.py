money_of_beggars = [int(x) for x in input().split(", ")]
count_of_beggars = int(input())
beggars = [0 for x in range(count_of_beggars)]
turn_of_beggars = 0

for current_money in range(len(money_of_beggars)):
    beggars[turn_of_beggars] += money_of_beggars[current_money]

    if turn_of_beggars == len(beggars) - 1:
        turn_of_beggars = 0
        continue

    turn_of_beggars += 1

print(beggars)


