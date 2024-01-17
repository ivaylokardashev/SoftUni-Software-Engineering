from collections import deque

command = input()
clients_queue = deque()

while command != "End":
    if command == "Paid":
        while len(clients_queue) != 0:
            print(clients_queue.popleft())
    else:
        clients_queue.append(command)

    command = input()
else:
    print(f'{len(clients_queue)} people remaining.')

