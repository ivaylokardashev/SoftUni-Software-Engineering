from collections import deque


COMPLETES = 4

fuel = [int(x) for x in input().split()]
consumption = deque([int(x) for x in input().split()])
needed_fuel = deque([int(x) for x in input().split()])


altitude = 0

for current_altitude in range(4):
    current_fuel = fuel.pop()
    current_consumption = consumption.popleft()
    current_needed_fuel = needed_fuel.popleft()

    left_fuel = current_fuel - current_consumption

    altitude = current_altitude + 1

    if left_fuel >= current_needed_fuel:
        print(f"John has reached: Altitude {altitude}")
    else:
        print(f"John did not reach: Altitude {altitude}")
        altitude -= 1
        break

if altitude == 0:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
elif altitude < COMPLETES:
    print(f"John failed to reach the top.")
    print(f"Reached altitudes: {', '.join([f'Altitude {n}' for n in range(1, altitude + 1)])}")
else:
    print("John has reached all the altitudes and managed to reach the top!")


