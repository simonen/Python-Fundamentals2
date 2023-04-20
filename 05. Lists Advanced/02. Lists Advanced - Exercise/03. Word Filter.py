words = input().split()

filtered = list(filter(lambda x: len(x) % 2 == 0, words))
for i in filtered:
    print(i)