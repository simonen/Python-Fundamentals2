deck = input().split()
shuffles = int(input())

for _ in range(shuffles):
    new_deck = []
    for i in range(0, len(deck) // 2):
        new_deck.append(deck[i])
        new_deck.append(deck[i + len(deck) // 2])
    deck = new_deck

print(deck)
