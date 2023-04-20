def sort_asc(num):
    number = list(map(int, num.split()))
    return sorted(number)


print(sort_asc(input()))