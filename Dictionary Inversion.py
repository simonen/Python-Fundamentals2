def dict_invert(book_f: dict):
    keys = list(book_f.keys())
    values = list(book_f.values())
    new_book = {}
    for i in range(len(values)):
        if values[i] not in new_book:
            new_book[values[i]] = []
        new_book[values[i]].append(keys[i])

    return new_book


book = {'Royal': 'Lighter', 'Ivan Ivanov': 'Red', 'DCay': 'Lighter', 'Palqk': 'Red'}
print(book)
newbook = dict_invert(book)
print(newbook)
