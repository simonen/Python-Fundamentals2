legendary = []
book = {'shards': 0, 'fragments': 0, 'motes': 0}
is_legend = False

while True:
    items = input().split()
    for i in range(0, len(items), 2):
        quantity = int(items[i])
        item = items[i + 1].lower()
        if item not in book:
            book[item] = 0
        book[item] += quantity
        if book['shards'] >= 250:
            legendary.append("Shadowmourne")
        elif book['fragments'] >= 250:
            legendary.append("Valanyr")
        elif book['motes'] >= 250:
            legendary.append("Dragonwrath")
        if len(legendary) > 0:
            print(f"{legendary[0]} obtained!")
            book[item] -= 250
            is_legend = True
            break
    if is_legend:
        break

for item, quantity in book.items():
    print(f"{item}: {quantity}")
