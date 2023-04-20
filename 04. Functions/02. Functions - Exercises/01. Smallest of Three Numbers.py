def smallest():
    nums = []
    for _ in range(3):
        nums.append(int(input()))
    return min(nums)


print(smallest())
