first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

# first_sequence = sorted(first_sequence)
# second_sequence = sorted(second_sequence)

for _ in range(int(input())):
    command, action, *numbers = input().split()
    # print(command, action, *numbers, sep=',')

    if command == "Add":
        if action == "First":
            for num in numbers:
                first_sequence.add(int(num))
        elif action == "Second":
            for num in numbers:
                second_sequence.add(int(num))

    elif command == "Remove":
        if action == "First":
            for num in numbers:
                # There have a problem when I try to remove element with remove()
                # discard() don't return error remove return error
                first_sequence.discard(int(num))
        elif action == "Second":
            for num in numbers:
                second_sequence.discard(int(num))

    elif command == "Check":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')