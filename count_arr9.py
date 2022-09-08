def count_arr9(arr):
    count = 0
    for num in arr:
        if num == 9:
            count +=1
    return count


arr1 = count_arr9([8,9,5,4])
arr2 = count_arr9([8,9,6,9])
print(arr1)
print(arr2)
print(count_arr9([6,9,3,9,2,9]))