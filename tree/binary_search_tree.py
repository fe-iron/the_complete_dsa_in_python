from Queue_and_stack import queue_using_LL

class BinarySearchTree:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

def insert(root, value):
    if not root:
        root.data = value
    if value <= root.data:
        if not root.left:
            root.left = BinarySearchTree(value)
        else:
            insert(root.left, value)
    else:
        if not root.right:
            root.right = BinarySearchTree(value)
        else:
            insert(root.right, value)


def pre_order_traversal(root):
    if not root:
        return
    print(root.data)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)


def post_order_traversal(root):
    if not root:
        return
    post_order_traversal(root.left)
    post_order_traversal(root.right)
    print(root.data)
    

def in_order_traversal(root):
    if not root:
        return
    in_order_traversal(root.left)
    print(root.data)
    in_order_traversal(root.rght)
    

def level_order_traversal(root):
    if not root:
        return
    queue = queue_using_LL.Queue()
    queue.enqueue(root)
    while not queue.isEmpty():
        temp_node = queue.dequeue()
        print(temp_node.data)
        if temp_node.left:
            queue.enqueue(temp_node.left)
        if temp_node.right:
            queue.enqueue(temp_node.right)


def search_node(root, value):
    if not root:
        return "no node in BST"
    queue = queue_using_LL.Queue()
    queue.enqueue(root)
    while not queue.isEmpty():
        temp_node = queue.dequeue()
        if temp_node.data == value:
            return f"{value} found"
        elif value < temp_node.data:
            if temp_node.left:
                queue.enqueue(temp_node.left)
        else:
            if temp_node.right:
                queue.enqueue(temp_node.right)
    return f"{value} not found"


def min_value_nnode(root):
    currennt = root
    while currennt.left:
        currennt = currennt.left
    return currennt


def delete_node(root, value):
    if not root:
        return root
    if value < root.data:
        root.left = delete_node(root.left, value)
    elif value > root.data:
        root.right = delete_node(root.right, value)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        if not root.right:
            temp = root.left
            root = None
            return temp
        temp = min_value_nnode(root)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)
    return root
        

def deleteBST(root):
    root = None
    root.left =None
    root.right = None
    return "Binary search tree successfully deleted"


bst = BinarySearchTree(60)
insert(bst, 50)
insert(bst, 30)
insert(bst, 70)
insert(bst, 30)
insert(bst, 10)
insert(bst, 90)
level_order_traversal(bst)
pre_order_traversal(bst)
post_order_traversal(bst)
search_node(bst, 70)
delete_node(bst, 10)
post_order_traversal(bst)