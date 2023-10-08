n_loops = int(input())
positive_list = []
negative_list = []
for current_loop in range(n_loops):
    number = int(input())
    if number >= 0:
        positive_list.append(number)
    else:
        negative_list.append(number)
print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")