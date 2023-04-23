array = list(map(int, input().split()))
command = input()

while command != "end":
    command = command.split()
    action = command[0]
    if action == "decrease":
        array = list(map(lambda x: x - 1, array))
        command = input()
        continue
    index1, index2 = int(command[1]), int(command[2])
    if action == "swap":
        array[index1], array[index2] = array[index2], array[index1]
    elif action == "multiply":
        array[index1] = array[index1] * array[index2]

    command = input()

print(", ".join(list(map(str, array))))
