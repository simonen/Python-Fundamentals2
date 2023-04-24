chest = input().split("|")
command = input()

while command != 'Yohoho!':
    command = command.split()
    action = command[0]
    if action == "Loot":
        loot = [x for x in command[1:] if x not in chest]
        chest = loot[::-1] + chest
    elif action == "Drop" and int(command[1]) <= len(chest) - 1:
        dropped_item = chest.pop(int(command[1]))
        chest.append(dropped_item)
    elif action == "Steal":
        stolen_count = int(command[1])
        stolen_loot = chest[-stolen_count:]
        chest = chest[:-stolen_count]
        print(", ".join(stolen_loot))

    command = input()

if len(chest) > 0:
    average_gain = len("".join(chest)) / len(chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
