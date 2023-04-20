# command = input()
# todo = []
# while command != "End":
#     todo.append(command)
#     command = input()
#
# todo_sorted = sorted(todo, key=lambda x: int(x.split("-")[0]))
# todos = [x.split("-")[1] for x in todo_sorted]
# print(todos)

command = input()
todo = [0] * 10

while command != "End":
    command = command.split("-")
    importance = int(command[0]) - 1
    task = command[1]
    todo.pop(importance)
    todo.insert(importance, task)

    command = input()

print([x for x in todo if x != 0])