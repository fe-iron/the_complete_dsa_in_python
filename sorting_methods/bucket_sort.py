import math


def inserton_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

def bucket_sort(nums):
    no_of_bucket = round(math.sqrt(len(nums)))
    max_value = max(nums)
    arr = []
    for i in range(no_of_bucket):
        arr.append([])
        
    for i in nums:
        index = math.ceil(i * no_of_bucket / max_value)
        arr[index - 1].append(i)

    for i in range(no_of_bucket):
        arr[i] = inserton_sort(arr[i])

    k = 0
    for i in range(no_of_bucket):
        for j in range(len(arr[i])):
            nums[k] = arr[i][j]
            k += 1
    print(nums)


def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    minValue = min(customList)
    maxValue = max(customList)
    rangeVal = (maxValue - minValue) / numberofBuckets
 
    buckets = [[] for _ in range(numberofBuckets)]
 
    for j in customList:
        if j == maxValue:
            buckets[-1].append(j)
        else:
            index_b = math.floor((j - minValue) / rangeVal)
            buckets[index_b].append(j)
    
    sorted_array = []
    for i in range(numberofBuckets):
        buckets[i] = inserton_sort(buckets[i])
        sorted_array.extend(buckets[i])
    
    return sorted_array

nums = [3,4,5,67,8,5,3,22,45,6,77,5,4]
print(nums)
bucket_sort(nums)



