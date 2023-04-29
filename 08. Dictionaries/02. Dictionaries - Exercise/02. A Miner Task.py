resource = input()

book = {}
while resource != "stop":
    quantity = int(input())
    if resource not in book:
        book[resource] = 0
    book[resource] += quantity

    resource = input()

for k, v in book.items():
    print(f"{k} -> {v}")
