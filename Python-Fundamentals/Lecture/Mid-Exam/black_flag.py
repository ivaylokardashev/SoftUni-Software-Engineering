days = int(input())
plunder_for_day = float(input())
goal = float(input())
total_plunder = 0

for day in range(1, days + 1):
    total_plunder += plunder_for_day

    if day % 3 == 0:
        total_plunder += plunder_for_day * 0.5

    if day % 5 == 0:
        total_plunder -= total_plunder * 0.3

if total_plunder >= goal:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage_to_rich_goal = total_plunder / goal * 100
    print(f"Collected only {percentage_to_rich_goal:.2f}% of the plunder.")
