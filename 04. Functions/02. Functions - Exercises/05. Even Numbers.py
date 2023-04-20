def evens(num):
    number = list(map(int, num.split()))
    even = list(filter(lambda x: x % 2 == 0, number))
    return even


print(evens(input()))
