team_A = [f"A-{str(n)}" for n in range(1, 12)]
team_B = [f"B-{str(n)}" for n in range(1, 12)]
red_cards = input().split(' ')

for i in red_cards:
    if i in team_A:
        team_A.remove(i)
    elif i in team_B:
        team_B.remove(i)

    if len(team_A) < 7 or len(team_B) < 7:
        print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
        print("Game was terminated")
        break
else:
    print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")



