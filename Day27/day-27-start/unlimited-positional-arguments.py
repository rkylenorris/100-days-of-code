def add(*nums):
    nums_sum = 0
    for n in nums:
        nums_sum += n
    return nums_sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
