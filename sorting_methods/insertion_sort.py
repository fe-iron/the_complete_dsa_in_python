def inserton_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

nums = [3,4,5,67,8,5,3,22,45,6,77,5,4]
print(nums)
inserton_sort(nums)