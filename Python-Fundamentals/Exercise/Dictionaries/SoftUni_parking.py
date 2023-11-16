parking = {}
n = int(input())

for index in range(n):
    command = input().split()

    if command[0] == "register":
        username = command[1]
        license_plate_number = command[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            print(f"{username} registered {license_plate_number} successfully")
            parking[f"{username}"] = license_plate_number
    elif command[0] == "unregister":
        username = command[1]
        if username in parking.keys():
            print(f"{username} unregistered successfully")
            parking.pop(username)
        else:
            print(f"ERROR: user {username} not found")

for (key, value) in parking.items():
    print(f"{key} => {value}")