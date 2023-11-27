explosion_string = input()
explosion_flag = False
explosions = 0
final_string = ""

for symbol in explosion_string:
    if symbol == ">":
        explosion_flag = True

    if explosion_flag and symbol != ">":
        if symbol.isdigit():
            explosions += int(symbol)
        if explosions > 0:
            explosion_string = explosion_string.replace(symbol, " ")
            explosions -= 1
            continue
        explosion_flag = False

    final_string += symbol

print(final_string)
