list_of_numbers = [int(s) for s in input().split(' ')]
count_of_numbers_to_remove = int(input())

for number in range(count_of_numbers_to_remove):
    list_of_numbers.remove(min(list_of_numbers))

for survival_numbers in range(len(list_of_numbers)):
    if survival_numbers == len(list_of_numbers) - 1:
        print(list_of_numbers[survival_numbers])
        break

    print(list_of_numbers[survival_numbers], end=", ")
