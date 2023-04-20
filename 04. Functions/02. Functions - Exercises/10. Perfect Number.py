def perfect_num(number_f):

    divisors = [x for x in range(1, number_f // 2 + 1) if number_f % x == 0]
    if sum(divisors) == number_f:
        # print("We have a perfect number!")
        # perfects.append(number_f)
        # print(perfects)
        return divisors
    # else:
        # print("It's not so perfect.")
    return None


perfects = []
for i in range(1, 100001):
    if perfect_num(i) is not None:
        print(i, perfect_num(i))
        perfects.append(i)

print(perfects)