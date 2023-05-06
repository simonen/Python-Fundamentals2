valid_chars = [range(48, 58), range(65, 91), range(97, 123), [45, 95]]
# chars = [chr(y) for x in valid_chars for y in x ]
# print(chars)
string = input().split(", ")
for word in string:
    if len(word) not in range(3, 17):
        continue
    for chars in word:
        if not any(ord(chars) in y for y in valid_chars):
            break
    else:
        print(word)
