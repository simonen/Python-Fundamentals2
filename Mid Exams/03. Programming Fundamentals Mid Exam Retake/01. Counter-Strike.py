energy = int(input())
distance = input()

wins = 0
while distance != "End of battle":
    if energy >= int(distance):
        wins += 1
        energy -= int(distance)
    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        break
    if wins % 3 == 0:
        energy += wins

    distance = input()

else:
    print(f"Won battles: {wins}. Energy left: {energy}")
