clothes = list(map(int, input().split()))
capacity = int(input())

racks = 0
sum_of_clothes = 0

while clothes:
    if sum_of_clothes + clothes[-1] > capacity:
        sum_of_clothes = 0
        racks += 1
    else:
        sum_of_clothes += clothes.pop()
        if not clothes:
            racks += 1

print(racks)
