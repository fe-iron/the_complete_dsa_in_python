def bubble_sort(num_list):
    for i in range(len(num_list)-1):
        for j in range(len(num_list)-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j], num_list[j]
    print(num_list)

nums = [3,4,5,67,8,5,3,22,45,6,77,5,4]
print(nums)
bubble_sort(nums)
