def add(x, y):
    return x + y


def subtract(add_f, z):
    return add_f - z


a = int(input())
b = int(input())
c = int(input())

print(subtract(add(a, b), c))
