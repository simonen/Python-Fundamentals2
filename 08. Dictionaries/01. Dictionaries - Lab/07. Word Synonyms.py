# n = int(input())
#
# words = {}
#
# for i in range(n):
#     word, synonym = input(), input()
#     if word not in words:
#         words[word] = []
#     words[word].append(synonym)
#
# for word, value in words.items():
#     print(f"{word} - {', '.join(value)}")

n = int(input())

synonyms = {}

for s in range(1, n + 1):

    key, value = input(), input()
    if key not in synonyms.keys():
        synonyms[key] = value
    else:
        if value not in synonyms.values():
            synonyms[key] += ", " + value

for key, value in synonyms.items():
    print(f"{key} - {value}")