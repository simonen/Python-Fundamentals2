integers = list(map(int, input().split()))

sum_removed = 0
while len(integers) > 0:
    index = int(input())
    if index < 0:
        removed = integers.pop(0)
        integers.insert(0, integers[-1])
    elif index > len(integers) - 1:
        removed = integers.pop(-1)
        integers.append(integers[0])
    else:
        removed = integers.pop(index)

    sum_removed += removed
    integers = list(map(lambda x: x + removed if x <= removed else x - removed, integers))

print(sum_removed)
