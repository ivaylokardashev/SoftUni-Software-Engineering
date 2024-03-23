from pprint import pp


def team_lineup(*args):
    players_by_country = dict()

    for index in range(len(args)):
        if not players_by_country.get(args[index][1]):
            players_by_country[args[index][1]] = []

        players_by_country[args[index][1]].append(args[index][0])

    sorted_players_by_country = sorted(players_by_country.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""

    for country, players in sorted_players_by_country:
        result += f"{country}:\n"
        for player_name in players:
            result += f"  -{player_name}\n"

    return result


print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))


