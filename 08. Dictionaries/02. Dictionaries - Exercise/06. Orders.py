command = input()
products = {}

while command != 'buy':
    command = command.split()
    product, price, quantity = command[0], float(command[1]), int(command[2])
    for i in range(0, len(command), 3):
        if product not in products:
            products[product] = [price, 0]
        products[product][1] += quantity
        products[product][0] = price

    command = input()

for k, v in products.items():
    print(f"{k} -> {(v[0] * v[1]):.2f}")
