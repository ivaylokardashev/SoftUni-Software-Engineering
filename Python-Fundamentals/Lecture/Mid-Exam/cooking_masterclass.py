from math import ceil


budget = float(input())
students = int(input())
price_for_package_flour = float(input())
price_for_single_egg = float(input())
price_for_single_apron = float(input())

price_of_ten_eggs = price_for_single_egg * 10
total_price_of_packages_flour = 0
total_price_of_eggs = price_of_ten_eggs * students
total_price_of_apron = price_for_single_apron * ceil(students + students * 0.20)

for current_student in range(1, students + 1):
    if current_student % 5 != 0:
        total_price_of_packages_flour += price_for_package_flour

total_cost_price = total_price_of_packages_flour + total_price_of_eggs + total_price_of_apron

if total_cost_price <= budget:
    print(f"Items purchased for {total_cost_price:.2f}$.")
else:
    print(f"{total_cost_price - budget:.2f}$ more needed.")
