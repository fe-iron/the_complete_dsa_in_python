def heapify(my_list, n, i):
    smallest = i
    l = i*2 + 1
    r = i*2 + 2
    if l < n and my_list[l] < my_list[smallest]:
        smallest = l
    if r < n and my_list[r] < my_list[smallest]:
        smallest = r
    if smallest != i:
        my_list[smallest], my_list[i] = my_list[i], my_list[smallest]
        heapify(my_list, n, smallest)


def heap_sort(my_list):
    n = len(my_list)
    for i in range(n//2-1, -1, -1):
        heapify(my_list, n, i)
    for i in range(n-1, 0, -1):
        my_list[i], my_list[0] = my_list[0], my_list[i]
        heapify(my_list, i, 0)
    return my_list


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
	print("%d" % arr[i],end=" ")

heap_sort(arr)