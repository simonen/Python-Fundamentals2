shopping_list = input().split("!")
command = input()

while command != "Go Shopping!":
    command = command.split()
    action = command[0]
    item = command[1]
    if action == "Urgent" and item not in shopping_list:
        shopping_list.insert(0, item)
    elif action == "Unnecessary" and item in shopping_list:
        shopping_list.remove(item)
    elif action == "Correct" and item in shopping_list:
        new_item = command[2]
        index = shopping_list.index(item)
        shopping_list[index] = new_item
    elif action == "Rearrange" and item in shopping_list:
        shopping_list.remove(item)
        shopping_list.append(item)

    command = input()

print(", ".join(shopping_list))
