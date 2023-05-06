string = input().split(">")
explosion = 0
for i, word in enumerate(string):
    if word[0].isdigit():
        boom = int(word[0])
        explosion += boom
        string[i] = word[explosion:]
        exploded = (len(word) - len(string[i]))
        explosion -= exploded

print(">".join(string))
