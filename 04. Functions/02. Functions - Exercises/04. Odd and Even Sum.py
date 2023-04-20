def odd_even_sum(num):
    number = list(map(int, list(num)))
    even = list(filter(lambda x: x % 2 == 0, number))
    odd = list(filter(lambda x: x % 2 != 0, number))
    return f"Odd sum = {sum(odd)}, Even sum = {sum(even)}"


print(odd_even_sum(input()))
