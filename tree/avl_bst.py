from Queue_and_stack import queue_using_LL

class AVL:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None
        self.height = 1

def pre_order_traversal(root):
    if not root:
        return "no node in AVL tree"
    print(root.data)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)


def post_order_traversal(root):
    if not root:
        return "no node in AVL tree"
    post_order_traversal(root.left)
    post_order_traversal(root.right)
    print(root.data)


def in_order_traversal(root):
    if not root:
        return "no node in AVL tree"
    in_order_traversal(root.left)
    print(root.data)
    in_order_traversal(root.right)


def level_order_traversal(root):
    if not root:
        return
    queue = queue_using_LL.Queue()
    queue.enqueue(root)
    while not queue.isEmpty():
        temp_node = queue.dequeue()
        print(temp_node.data)
        if temp_node.left:
            queue.enqueue(root.left)
        if temp_node.right:
            queue.enqueue(root.right)


def search(root, value):
    if root.data == value:
        return f"{value} found at root"
    if value < root.data:
        if value == root.left.data:
            return f"{value} found in left tree"
        else:
            search(root.left, value)
    elif value > root.data:
        if value == root.right.data:
            return f"{value} found in right tree"
        else:
            search(root.right, value)

def get_height(root):
    if not root:
        return 0
    return root.height


# left left condition
def rotate_right(disbalanced_node):
    new_node = disbalanced_node.left
    disbalanced_node.left = disbalanced_node.left.right
    new_node.right = disbalanced_node
    # update height disbalanced node and new root
    new_node.height = 1 + max(get_height(new_node.left), get_height(new_node.right))
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left), get_height(disbalanced_node.right))
    return new_node

# left right condition
def rotate_left(disbalanced_node):
    new_node = disbalanced_node.right
    disbalanced_node.right = disbalanced_node.right.left
    new_node.left = disbalanced_node
    # update height disbalanced node and new root
    new_node.height = 1 + max(get_height(new_node.left), get_height(new_node.right))
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left), get_height(disbalanced_node.right))
    return new_node

def get_balance(root):
    if not root:
        return 0
    return get_height(root.left) - get_height(root.right)


def insert(root, value):
    if not root:
        return AVL(value)
    elif value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    # left left condition
    if balance > 1 and value < root.left.data:
        return rotate_right(root)
    # left right condition
    if balance > 1 and value > root.left.data:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    # right right condition
    if balance < -1 and value > root.right.data:
        return rotate_left(root)
    # right left condition
    if balance < -1 and value < root.right.data:
        root.right = rotate_right(root.right)
        return rotate_left(root)
    return root

def get_min_value(root):
    if root is None or root.left is None:
        return root
    get_min_value(root.left)
     
def delete_node(root, value):
    if not root:
        return root
    elif value < root.data:
        root.left = delete_node(root.left, value)
    elif value > root.data:
        root.right = delete_node(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = get_min_value(root.right)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)
    root.height = 1 - max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    # left left condition
    if balance > 1 and get_balance(root.left) >= 0:
        return rotate_right(root)
    # right right condition
    if balance < -1 and get_balance(root.right) <= 0:
        return rotate_left(root)
    # left right condition
    if balance > 1 and get_balance(root.left) < 0:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    # right left condition
    if balance < -1 and get_balance(root.right) > 0:
        root.right = rotate_right(root.right)
        return rotate_left(root)
    return root

def deleteAVL(root):
    root.data = None
    root.left = None
    root.right = None
    return "AVL BST deleted"

avl = AVL(5)
avl = insert(avl, 10)
avl = insert(avl, 15)
avl = insert(avl, 20)
level_order_traversal(avl)
pre_order_traversal(avl)
post_order_traversal(avl)
delete_node(avl, 15)
in_order_traversal(avl)
deleteAVL(avl)