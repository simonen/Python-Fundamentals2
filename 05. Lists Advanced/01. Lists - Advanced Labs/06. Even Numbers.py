numbers = list(map(int, input().split(", ")))

# even_in = [x for x, y in enumerate(numbers) if y % 2 == 0]

# print(even_in)

indices = list(map(lambda x: x if numbers[x] % 2 == 0 else 'no', range(len(numbers))))
ind = list(filter(lambda x: x != 'no', indices))

print(ind)