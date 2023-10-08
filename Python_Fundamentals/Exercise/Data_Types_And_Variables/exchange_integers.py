first_num = int(input())
second_num = int(input())

print(f"Before:\na = {first_num}\nb = {second_num}")

first_num, second_num = second_num, first_num

print(f"After:\na = {first_num}\nb = {second_num}")