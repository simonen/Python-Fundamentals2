line = input().split()
search = input().split()

products = {}

for i in range(0, len(line), 2):
    key = line[i]
    value = line[i + 1]
    products[key] = value

for k in search:
    if k in products.keys():
        print(f'We have {products[k]} of {k} left')
    else:
        print(f"Sorry, we don't have {k}")