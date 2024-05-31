def selection_sort(nums):
    for i in range(len(nums)):
        min_num = i
        for j in range(i+1, len(nums)):
            if nums[min_num] > nums[j]:
                nums[min_num], nums[j] = nums[j], nums[min_num]
    print(nums)


nums = [3,4,5,67,8,5,3,22,45,6,77,5,4]
print(nums)
selection_sort(nums)