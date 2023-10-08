def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid_index = (low + high) // 2
        mid_element = numbers[mid_index]

        if mid_element == target:
            return mid_index

        if mid_element > target:
            high = mid_index - 1
        else:
            low = mid_index + 1


try:
    target_flag = True
    target = int(input())
    target_flag = False
    numbers = [int(x) for x in input().split(', ')]

    if binary_search(numbers, target) is None:
        print("Target is not found")
    else:
        print(f"Index - {binary_search(numbers, target)}")

except ValueError:
    if target_flag:
        print("You have to enter a single integer number!")
    else:
        print("Your notation which separate numbers list is wrong! You have to add after all numbers except last ', '.")


