string = input().split()

longer = string[0]
shorter = string[1]
if len(shorter) > len(longer):
    longer, shorter = string[1], string[0]

result = 0
n = len(shorter)
pairs = list(zip(longer[:n], shorter))
for i in pairs:
    result += ord(i[0]) * ord(i[1])

result += sum([ord(x) for x in longer[n:]])
print(result)
