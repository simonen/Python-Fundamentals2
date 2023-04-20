def trib(nums):
    starting = [1, 1, 2]
    for i in range(0, nums - 3):
        starting.append(sum(starting[i:i + 3]))

    return " ".join(list(map(str, starting))[:nums])


print(trib(int(input())))
