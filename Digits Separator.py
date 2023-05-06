def separator(string_f):
    rage = []
    subs = ''
    n = ''
    for i, char in enumerate(string_f):
        if not char.isdigit():
            subs += char
            if len(n) > 0:
                rage.append(n)
            n = ''
            if i + 1 == len(string_f):
                rage.append(subs)
        else:
            if len(subs) > 0:
                rage.append(subs)
            subs = ''
            n += char
            if i + 1 == len(string_f):
                rage.append(n)

    return rage


string = '9asd141a111a2'

print(separator(string))
