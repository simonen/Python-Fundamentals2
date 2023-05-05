book = {}
n = int(input())

for i in range(n):
    dragon = input().split()
    color, name, damage, health, armor = dragon
    if color not in book:
        book[color] = {}
    if damage == 'null':
        damage = 45
    if health == 'null':
        health = 250
    if armor == 'null':
        armor = 10
    if name not in book[color]:
        book[color][name] = []
    book[color][name] = list(map(int, [damage, health, armor]))

for color, dragonz in book.items():
    average = [0, 0, 0]
    dragon_count = len(dragonz)
    for x in list(dragonz.values()):
        for i in range(3):
            average[i] += x[i] / dragon_count
    average = [f"{x:.2f}" for x in average]
    print(f"{color}::({'/'.join(average)})")
    for name, stats in sorted(dragonz.items(), key=lambda x: x):
        print(f"-{name} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}")
