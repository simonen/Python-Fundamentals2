def dict_invert(book_f: dict):
    keys = [x for x in book_f.keys()]
    values = [x for x in book_f.values()]
    new_book = {}
    for i in range(len(values)):
        if values[i] not in new_book:
            new_book[values[i]] = []
        new_book[values[i]].append(keys[i])

    return new_book


book = {'Royal': 'Lighter', 'Ivan Ivanov': 'Lighter', 'DCay': 'Lighter', 'Palqk': 'Red'}

print(dict_invert(book))