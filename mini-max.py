def miniMaxSum(arr):
    # Write your code here
    min = sum (arr [:2])
    max = sum(arr[1:])

    return (min, max)

list = miniMaxSum([1, 2, 15, 3])
print(list)