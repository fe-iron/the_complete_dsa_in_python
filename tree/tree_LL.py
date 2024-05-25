from Queue_and_stack import queue_using_LL

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left  =None

def preorder_traversal(root):
    if not root:
        return
    print(root.data)
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)

def postorder_traversal(root):
    if not root:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data)
    

def level_order_traversal(root):
    if not root:
        return
    queue = queue_using_LL.Queue()
    queue.enqueue(root)
    while not queue.isEmpty():
        temp_root = queue.dequeue()
        print(temp_root.data)
        if temp_root.left:
            queue.enqueue(temp_root.left)
        if temp_root.right:
            queue.enqueue(temp_root.right)
    

def searchBT(root_node, node_value):
    if not root_node:
        return "node not found"
    queue = queue_using_LL.Queue()
    queue.enqueue(root_node)
    while not queue.isEmpty():
        temp_node = queue.dequeue()
        if temp_node.data == node_value:
            return "Success"
        if temp_node.right:
            queue.enqueue(temp_node.right)
        if temp_node.left:
            queue.enqueue(temp_node.left)
    return "not found"

def insert_node(root_node, new_node):
    if not root_node:
        root_node = new_node
        return "root inserted"
    queue = queue_using_LL.Queue()
    queue.enqueue(root_node)
    while not queue.isEmpty():
        temp_node = queue.dequeue()
        if temp_node.left:
            queue.enqueue(temp_node.left)
        else:
            temp_node.left = new_node
            return "left inserted"
        if temp_node.right:
            queue.enqueue(temp_node.right)
        else:
            temp_node.right = new_node
            return "right inserted" 
    return "not inserted"
        
def get_deepest_node(root_node):
    if not root_node:
        return "no node in tree"
    queue = queue_using_LL.Queue()
    queue.enqueue(root_node)
    while not queue.isEmpty():
        temp_node = queue.dequeue()
        if temp_node.left:
            queue.enqueue(temp_node.left)
        if temp_node.right:
            queue.enqueue(temp_node.right)
    return temp_node


def delete_deepest_node(root_node, deepest_node):
    if not root_node:
        return "no node in tree"
    queue = queue_using_LL.Queue()
    queue.enqueue(root_node)
    while not queue.isEmpty():
        temp_node = queue.dequeue()
        if temp_node == deepest_node:
            temp_node = None
            return "deleted"
        if temp_node.left:
            if temp_node.left == deepest_node:
                temp_node.left = None
                return "deleted left"
            else:
                queue.enqueue(temp_node.left)
        if temp_node.right:
            if temp_node.right == deepest_node:
                temp_node.right = None
                return "deleted right"
            else:
                queue.enqueue(temp_node.right)
    return "node not found"


def delete_node(root_node, delete_node):
    if not root_node:
        return "BT is not present"
    queue = queue_using_LL.Queue()
    queue.enqueue(root_node)
    while not queue.isEmpty():
        temp_node = queue.dequeue()
        if temp_node.data == delete_node:
            d_node = get_deepest_node(root_node)
            temp_node.data = d_node.data
            delete_deepest_node(root_node, d_node)
            return "the node has been successfully deleted"
        if root_node.left:
            queue.enqueue(temp_node.left)
        if root_node.right:
            queue.enqueue(temp_node.right)
    return "failed to delete"


def deleteBT(root_node):
    root_node = None
    root_node.right = None
    root_node.left = None
    return "Binary tree deleted"



tree = TreeNode("drinks")
hot = TreeNode("hot")
cold = TreeNode("cold")

tree.left = hot
tree.right = cold
preorder_traversal(tree)
inorder_traversal(tree)
postorder_traversal(tree)
level_order_traversal(tree)
searchBT(tree, "drinks")
chai = TreeNode("chai")
insert_node(tree, chai)
inorder_traversal(tree)
deep_node = get_deepest_node(tree)
print(deep_node.data)
# delete_deepest_node(tree, deep_node)
delete_node(tree, "hot")
level_order_traversal(tree)