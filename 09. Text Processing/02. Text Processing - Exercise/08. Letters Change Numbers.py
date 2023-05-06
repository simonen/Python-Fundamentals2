string = input().split()

alphabet = [chr(x) for x in range(96, 123)]
total = 0

for substring in string:
    number = int(substring[1:-1])
    left_letter = substring[0]
    right_letter = substring[-1]
    index_left = alphabet.index(left_letter.lower())
    index_right = alphabet.index(right_letter.lower())
    if left_letter.isupper():
        total /= index_left
    elif left_letter.islower():
        total *= index_left
    if right_letter.isupper():
        total -= index_right
    elif right_letter.islower():
        total += index_right

print(f"{total:.2f}")
