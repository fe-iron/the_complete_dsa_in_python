class Heap:
    def __init__(self, size) -> None:
        self.custom_list = (size + 1) * [None]
        self.max_size = size + 1
        self.heap_size = 0

def peek(root):
    if not root:
        return
    return root.custom_list[1]

def heap_size(root):
    if not root:
        return 0
    return root.heap_size

def level_order_traversal(root):
    if not root:
        return
    for i in range(1, root.heap_size+1):
        print(root.custom_list[i])

def heapify_insert(root, index, heap_type):
    parent_index = index // 2
    if index <= 1:
        return
    if heap_type == "Min":
        if root.custom_list[index] < root.custom_list[parent_index]:
            temp = root.custom_list[index]
            root.custom_list[index] = root.custom_list[parent_index]
            root.custom_list[parent_index] = temp
        heapify_insert(root, parent_index, heap_type)
    elif heap_type == "Max":
        if root.custom_list[index] > root.custom_list[parent_index]:
            temp = root.custom_list[index]
            root.custom_list[index] = root.custom_list[parent_index]
            root.custom_list[parent_index] = temp
        heapify_insert(root, parent_index, heap_type)

    
def insert(root, value, heap_type):
    if root.heap_size + 1 == root.max_size:
        return "heap is full"
    root.custom_list[root.heap_size + 1] = value
    root.heap_size += 1
    heapify_insert(root, root.heap_size, heap_type)
    return f"{value} is inserted"
    

def heapify_tree_extract(root, index, heap_type):
    left_index = index * 2
    right_index = index * 2 + 1
    swap_child = 0
    if root.heap_size < left_index:
        return
    elif root.heap_size == left_index:
        if heap_type == "Min":
            if root.custom_list[index] > root.custom_list[left_index]:
                temp = root.custom_list[index]
                root.custom_list[index] = root.custom_list[left_index]
                root.custom_list[left_index] = temp
            return
        else:
            if root.custom_list[index] < root.custom_list[left_index]:
                temp = root.custom_list[index]
                root.custom_list[index] = root.custom_list[left_index]
                root.custom_list[left_index] = temp
            return
    else:
        if heap_type == "Min":
            if root.custom_list[left_index] < root.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if root.custom_list[index] > root.custom_list[swap_child]:
                temp = root.custom_list[index]
                root.custom_list[index] = root.custom_list[swap_child]
                root.custom_list[swap_child] = temp
        else:
            if root.custom_list[left_index] > root.custom_list[right_index]:
                swap_child = left_index
            else:
                swap_child = right_index
            if root.custom_list[index] < root.custom_list[swap_child]:
                temp = root.custom_list[index]
                root.custom_list[index] = root.custom_list[swap_child]
                root.custom_list[swap_child] = temp
        heapify_tree_extract(root, swap_child, heap_type)

def extract_node(root, heap_type):
    if root.heap_size == 0:
        return 
    else:
        extracted_value = root.custom_list[1]
        root.custom_list[1] = root.custom_list[root.heap_size]
        root.heap_size -= 1
        heapify_tree_extract(root, 1, heap_type)
        return extracted_value

def delete(root):
    root.custom_list = None
    return "Heap Binary Tree is deleted"

heap_tree = Heap(10)
peek(heap_tree)
heap_size(heap_tree)
insert(heap_tree, 4, "Max")
insert(heap_tree, 5, "Max")
insert(heap_tree, 12, "Max")
insert(heap_tree, 4, "Max")
insert(heap_tree, 4, "Max")
insert(heap_tree, 4, "Max")
insert(heap_tree, 4, "Max")
insert(heap_tree, 4, "Max")
insert(heap_tree, 4, "Max")
insert(heap_tree, 1, "Max")
level_order_traversal(heap_tree)
print(extract_node(heap_tree, "Max"))
level_order_traversal(heap_tree)
delete(heap_tree)
