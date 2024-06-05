import math


def binary_search(arr, num):
    if not arr:
        return "no elemnet in array"
    start = 0
    end = len(arr) - 1
    mid = math.floor((start + end)/2)
    while not num == arr[mid] and start <= end:
        if num > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = math.floor((start + end) / 2)
    return mid


arr = [1,2,4,5,6,7,88,654,4,5,7,7,4,3,3,3]
arr.sort()
binary_search(arr, -5)