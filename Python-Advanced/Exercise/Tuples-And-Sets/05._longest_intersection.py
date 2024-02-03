import re

longest_intersection = []

for _ in range(int(input())):
    data = list(map(int, re.split(f"-|,", input())))

    data = [max(data[0], data[2]), min(data[1], data[3])]

    if len(longest_intersection) == 0:
        longest_intersection = data

    range_of_longest_intersection = (longest_intersection[1] + 1) - longest_intersection[0]
    range_of_data_intersection = (data[1] + 1) - data[0]

    if range_of_data_intersection > range_of_longest_intersection:
        longest_intersection = data

print(f"Longest intersection is {[x for x in range(longest_intersection[0], longest_intersection[1] + 1, 1)]}"
      f" with length {(longest_intersection[1] - longest_intersection[0] + 1)}")
