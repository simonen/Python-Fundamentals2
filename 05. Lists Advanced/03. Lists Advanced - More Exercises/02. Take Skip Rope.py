string = list(input())

digits = [int(x) for x in string if x.isdigit()]
non_digits = [x for x in string if not x.isdigit()]
new_string = ''
index = 0

for i in range(len(digits)):
    if i % 2 == 0:
        new_string += "".join(non_digits[index:index + digits[i]])
    index += digits[i]

print(new_string)
