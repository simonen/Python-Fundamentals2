targets = list(map(int, input().split()))
index = input()

while index != "End":
    index = int(index)
    if index not in range(len(targets)):
        index = input()
        continue

    value = targets[index]
    if value != -1:
        targets = list(map(lambda x: x - value if x > value and x != -1 else x + value if x != -1 else x, targets))
        targets[index] = -1

    index = input()

print(f"Shot targets: {targets.count(-1)} -> {' '.join(list(map(str, targets)))}")
