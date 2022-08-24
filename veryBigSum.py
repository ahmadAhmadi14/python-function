def veryBigSum(*a):
    nums = 0
    for i in range(0, len(a)):
        nums += a[i]
    return nums

list =veryBigSum(1000000001, 1000000002, 1000000003, 1000000004, 1000000005)
print(list)
