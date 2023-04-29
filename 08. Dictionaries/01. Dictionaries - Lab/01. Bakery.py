line = 'bread 10 butter 4 sugar 9 jam 12'.split()
bakery = {}

for i in range(0, len(line), 2):
    key = line[i]
    value = line[i + 1]
    bakery[key] = value

print(bakery)