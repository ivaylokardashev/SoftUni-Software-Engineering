miner_bag = {}
while True:
    command = input()

    if command == "stop":
        break

    quantity = int(input())

    if command not in miner_bag.keys():
        miner_bag[f"{command}"] = 0

    miner_bag[f"{command}"] += quantity

for (key, value) in miner_bag.items():
    print(f"{key} -> {value}")

