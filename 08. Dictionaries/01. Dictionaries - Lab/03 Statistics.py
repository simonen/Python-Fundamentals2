command = input()

products = {}
print("Products in stock:")

while command != 'statistics':
    command = command.split(": ")
    product, quantity = command[0], int(command[1])
    if product not in products:
        products[product] = 0
    products[product] += quantity

    command = input()

for k, v in products.items():
    print(f" - {k}: {v}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
