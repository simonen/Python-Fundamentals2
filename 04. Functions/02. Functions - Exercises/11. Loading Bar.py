def loading(number):
    if number in range(0, 91, 10):
        percents = '%' * (number // 10)
        print(f"{number}% [{percents:.<10}]\n"
              f"Still loading...")
    elif number == 100:
        print("100% Complete!\n"
              f"[{'':%<10}]")


num = int(input())

loading(num)
