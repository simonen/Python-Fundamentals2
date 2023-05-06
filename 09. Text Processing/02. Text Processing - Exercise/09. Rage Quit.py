string = input()

uniq = []
rage = []
subs = ''
n = ''
for i, char in enumerate(string):
    if char.lower() not in uniq and not char.isdigit():
        uniq.append(char.lower())
    if not char.isdigit():
        subs += char
        if len(n) > 0:
            rage.append(n)
        n = ''
    else:
        if len(subs) > 0:
            rage.append(subs.upper())
        subs = ''
        n += char
    if i + 1 == len(string):
        rage.append(n)

ragequit = ''
for i in range(0, len(rage), 2):
    ragequit += rage[i] * int(rage[i + 1])

print(f"Unique symbols used: {len(uniq)}\n"
      f"{ragequit}")
