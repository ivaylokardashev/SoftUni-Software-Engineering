countries_and_capitals = {country: capital for (country, capital) in zip(input().split(', '), input().split(', '))}

for (country, capital) in countries_and_capitals.items():
    print(f"{country} -> {capital}")
