targets = list(map(int, input().split()))
command = input()

while command != 'End':
    command = command.split()
    action = command[0]
    index = int(command[1])
    if action == 'Add':
        if index in range(len(targets)):
            value = int(command[2])
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Shoot" and index in range(len(targets)):
        power = int(command[2])
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
    elif action == "Strike":
        radius = int(command[2])
        if index + radius in range(len(targets)) and index - radius in range(len(targets)):
            targets = targets[:index - radius] + targets[index + radius + 1:]
        else:
            print("Strike missed!")

    command = input()

print("|".join(list(map(str, targets))))
