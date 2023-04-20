integers = list(map(int, input().split(", ")))
beggars = int(input())

pot = []

for i in range(0, beggars):
    pot.append(sum(integers[i::beggars]))

print(pot)

