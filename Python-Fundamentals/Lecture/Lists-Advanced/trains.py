wagons = int(input())
passengers_in_wagons = [0 for x in range(wagons)]

while True:
    command = input()

    if command == "End":
        break

    command_for_passengers = [x for x in command.split(" ")]

    if command_for_passengers[0] == "add":
        people = int(command_for_passengers[1])

        passengers_in_wagons[len(passengers_in_wagons) - 1] = people

    elif command_for_passengers[0] == "insert":
        wagon = int(command_for_passengers[1])
        people = int(command_for_passengers[2])

        passengers_in_wagons[wagon] = people

    elif command_for_passengers[0] == "leave":
        wagon = int(command_for_passengers[1])
        people = int(command_for_passengers[2])

        passengers_in_wagons[wagon] -= people

print(passengers_in_wagons)

