even_set = set()
odd_set = set()

for current_row in range(1, (int(input()) + 1), 1):
    name = input()

    sum_of_letters = sum([ord(l) for l in name])

    sum_of_letters /= current_row
    sum_of_letters = int(sum_of_letters)

    if sum_of_letters % 2 == 0:
        even_set.add(sum_of_letters)
    else:
        odd_set.add(sum_of_letters)

if sum(even_set) == sum(odd_set):
    print(*(even_set.union(odd_set)), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*(odd_set.difference(even_set)), sep=', ')
else:
    print(*(even_set.symmetric_difference(odd_set)), sep=', ')
