command = input()

book = {}

while command != "End":
    company, eid = command.split(" -> ")
    if company not in book:
        book[company] = []
    if eid not in book[company]:
        book[company].append(eid)

    command = input()

for company, eid in book.items():
    joined = '\n-- '.join(eid)
    print(f"{company}\n"
          f"-- {joined}")
