number_of_snowballs = int(input())
max_weight_of_snowball = 0
max_time_needed = 0
max_quality = 0
max_value = 0

for snowball in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (weight_of_snowball / time_needed) ** quality

    if max_value < value:
        max_weight_of_snowball = weight_of_snowball
        max_time_needed = time_needed
        max_quality = quality
        max_value = value

print(f"{max_weight_of_snowball} : {max_time_needed} = {int(max_value)} ({max_quality})")