def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def get_pivot(my_list, pivot_start, pivot_end):
    swap_index = pivot_start
    for i in range(pivot_start+1, pivot_end+1):
        if my_list[i] < my_list[pivot_start]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_start, swap_index)
    return swap_index


def quick_sort(my_list, left, right):
    if left < right:
        pivot_index = get_pivot(my_list, left, right)
        quick_sort(my_list, left, pivot_index-1)
        quick_sort(my_list, pivot_index+1, right)
    return my_list


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
	print("%d" % arr[i],end=" ")

quick_sort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
	print("%d" % arr[i],end=" ")