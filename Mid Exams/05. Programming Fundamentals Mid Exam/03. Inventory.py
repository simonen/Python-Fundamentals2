items = input().split(", ")
command = input()

while command != "Craft!":
    command = command.split(" - ")
    action = command[0]
    item = command[1]
    if action == "Collect" and item not in items:
        items.append(item)
    elif action == "Drop" and item in items:
        items.remove(item)
    elif action == "Combine Items" and item.split(":")[0] in items:
        old_item = item.split(":")[0]
        new_item = item.split(":")[1]
        old_index = items.index(old_item)
        items.insert(old_index + 1, new_item)
    elif action == "Renew" and item in items:
        items.remove(item)
        items.append(item)

    command = input()

print(", ".join(items))
