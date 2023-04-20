integers = list(map(int, input().split()))
command = input()

while command != "end":
    rindex = None
    command = command.split()
    action = command[0]

    if action == "exchange":
        index = int(command[1])
        if 0 <= index <= len(integers) - 1:
            integers = integers[index + 1:] + integers[:index + 1]
        else:
            print("Invalid index")

    if any(x == "even" for x in command):
        even = list(filter(lambda x: x % 2 == 0, integers))
    elif any(x == "odd" for x in command):
        odd = list(filter(lambda x: x % 2 != 0, integers))

    if action == "max":
        odd_even = command[1]
        if odd_even == "even" and len(even) > 0:
            rindex = len(integers) - integers[::-1].index(max(even)) - 1
        elif odd_even == "odd" and len(odd) > 0:
            rindex = len(integers) - integers[::-1].index(max(odd)) - 1

    elif action == "min":
        odd_even = command[1]
        if odd_even == "even" and len(even) > 0:
            rindex = len(integers) - integers[::-1].index(min(even)) - 1
        elif odd_even == "odd" and len(odd) > 0:
            rindex = len(integers) - integers[::-1].index(min(odd)) - 1

    if action == "min" or action == "max":
        if rindex is None:
            print("No matches")
        else:
            print(rindex)

    if action == "first" or action == "last":
        count = int(command[1])
        if count > len(integers):
            print("Invalid count")
            command = input()
            continue

    if action == "first":
        if command[2] == "even":
            print(even[:count])
        elif command[2] == "odd":
            print(odd[:count])

    elif action == "last":
        if command[2] == "even":
            print(even[-count:])
        elif command[2] == "odd":
            print(odd[-count:])

    command = input()

print(integers)