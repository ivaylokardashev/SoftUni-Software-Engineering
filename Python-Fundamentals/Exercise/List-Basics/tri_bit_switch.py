def switch_tri_bit(number, position):
    mask = 7 << position
    result = number ^ mask

    print(result)


switch_tri_bit(44444, 4)
