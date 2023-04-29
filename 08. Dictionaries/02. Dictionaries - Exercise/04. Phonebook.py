entry = input()
phonebook = {}

while not entry.isdigit():
    entry = entry.split("-")
    name, number = entry[0], entry[1]
    phonebook[name] = number

    entry = input()

for i in range(int(entry)):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
