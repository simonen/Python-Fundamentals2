string = input()

prev = ''
new = ''
for i, letter in enumerate(string):
    if letter != prev:
        new += letter

    prev = letter

print(new)