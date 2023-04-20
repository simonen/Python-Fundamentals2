names = input().split(", ")

A = sorted(names, key=lambda x: (-len(x), x))
print(A)