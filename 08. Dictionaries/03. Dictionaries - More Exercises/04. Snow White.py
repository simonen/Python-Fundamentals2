book = {}
command = input()

while command != "Once upon a time":
    name, color, height = command.split(" <:> ")
    if color not in book:
        book[color] = {}
    if name not in book[color] or book[color][name] < int(height):
        book[color][name] = int(height)

    command = input()

highest = [[color, y, t] for color, z in sorted(book.items(), key=lambda a: -len(a[1])) for y, t in z.items()]

for color, name, height in sorted(highest, key=lambda x: -x[2]):
    print(f"({color}) {name} <-> {height}")
