rows = int(input())

ships = []

for i in range(rows):
    ships.append(list(map(int, input().split())))

destroyed_ships = 0
attacks = input().split()

for j in attacks:
    square_shot = j.split("-")
    if ships[int(square_shot[0])][int(square_shot[1])] > 0:
        ships[int(square_shot[0])][int(square_shot[1])] -= 1
        if ships[int(square_shot[0])][int(square_shot[1])] == 0:
            destroyed_ships += 1

print(destroyed_ships)
