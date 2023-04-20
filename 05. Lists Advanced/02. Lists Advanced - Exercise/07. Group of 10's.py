numbers = list(map(int, input().split(", ")))

max_num = max(numbers)

for i in range(10, max_num + 10, 10):
    group = [x for x in numbers if i - 10 < x <= i]
    print(f"Group of {i}'s: {group}")
