from collections import deque


people_queue = deque()
litters_of_water = int(input())
command = input()

while command != 'Start':
    people_queue.append(command)

    command = input()

command = input().split()

while command[0] != "End":

    if command[0].isdigit():
        litters_to_be_removed = int(command[0])

        if litters_of_water >= litters_to_be_removed:
            person_name = people_queue.popleft()
            litters_of_water -= litters_to_be_removed
            print(f'{person_name} got water')
        else:
            person_name = people_queue.popleft()
            print(f"{person_name} must wait")
    elif command[0] == 'refill':
        _, litters_to_be_added = command[0], int(command[1])
        litters_of_water += litters_to_be_added

    command = input().split()

print(f"{litters_of_water} liters left")
