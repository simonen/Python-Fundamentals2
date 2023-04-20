def multsign():
    nums = []
    for i in range(3):
        nums.append(int(input()))
    if any(x == 0 for x in nums):
        return "zero"

    negatives = list(filter(lambda x: x < 0, nums))
    if len(negatives) % 2 != 0:
        return "negative"

    return "positive"


print(multsign())