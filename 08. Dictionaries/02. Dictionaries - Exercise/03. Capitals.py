countries = input().split(", ")
capitals = input().split(", ")

diction = dict(zip(countries, capitals))

for country, capital in diction.items():
    print(f"{country} -> {capital}")
