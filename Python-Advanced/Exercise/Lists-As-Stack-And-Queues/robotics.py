from collections import deque
from datetime import datetime, timedelta


robots = {robot: [int(seconds), 0] for item in input().split(';') for robot, seconds in [item.split('-')]} # {"ROB": [15,0]}
factory_time = datetime.strptime(input(), "%H:%M:%S") # datetime object, factory_time = 8:00:00

products = deque()

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    factory_time += timedelta(seconds=1)    # Add one second to factory_time = 8:00:01
    product = products.popleft()

    free_robots = []    # List for all free robots

    for name, value in robots.items():
        if value[1] != 0:   # Check if robot have task
            robots[name][1] -= 1

        if value[1] == 0:   # Check if robot end his task if it is end task it's appended to free_robots
            free_robots.append([name, value])

    if not free_robots: # Check if there haven't free robots
        products.append(product)    # Product is append in the end because have not free robots
        continue

    robot_name, data = free_robots[0]   # take name and data of free robots
    robots[robot_name][1] = data[0] # data[1] take data[0] the time to perfom its task cause it get new task

    print(f"{robot_name} - {product} [{factory_time.strftime('%H:%M:%S')}]")    # Print data and format time cause we don't need year, month and day
