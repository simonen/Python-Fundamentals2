command = input()
customer_type = ['special', 'regular']
total_price = 0

while command not in customer_type:
    price = 0
    if '-' not in command:
        price = float(command)
    else:
        print("Invalid price!")

    total_price += price
    command = input()

if total_price == 0:
    print("Invalid order!")
else:
    taxes = total_price * 0.2
    grand_total = total_price * 1.2
    if command == 'special':
        grand_total *= 0.9
    print("Congratulations you've just bought a new computer!\n"
          f'Price without taxes: {total_price:.2f}$\n'
          f'Taxes: {taxes:.2f}$\n'
          '-----------\n'
          f'Total price: {grand_total:.2f}$')
