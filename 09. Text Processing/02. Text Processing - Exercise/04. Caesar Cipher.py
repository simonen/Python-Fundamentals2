text = input()

encrypted = ''

for i in text:
    encrypted += chr(ord(i) + 3)

print(encrypted)