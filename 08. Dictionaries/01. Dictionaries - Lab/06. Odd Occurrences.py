line = input().split()

elements = {}

for i in line:
    key = i.lower()
    if key not in elements:
        elements[key] = 0
    elements[key] += 1


odds = [x for x in elements if elements[x] % 2 != 0]
print(" ".join(odds))
