secret = input().split()
decoded_msg = []

for word in secret:
    decoded_word = ''
    ascii_code = "".join([x for x in word[:3] if x.isdigit()])
    letters = [x for x in word if x.isalpha()]
    letters[0], letters[-1] = letters[-1], letters[0]
    first_letter = chr(int(ascii_code))
    decoded_word += first_letter + "".join(letters)
    decoded_msg.append(decoded_word)

print(" ".join(decoded_msg))
