def arr_to_three(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False


print(arr_to_three([5,6,7,9,1,2,3]))
print(arr_to_three([5,6,8,1,2,-3]))