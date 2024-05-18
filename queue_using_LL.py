class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)
    

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        temp_node = self.head
        while temp_node:
            yield temp_node
            temp_node = temp_node.next

    
class Queue:
    def __init__(self) -> None:
        self.linked_list = LinkedList()
    
    def __str__(self):
        result = [str(x) for x in self.linked_list]
        return " <- ".join(result)
    
    def enqueue(self, value):
        new_node = Node(value)
        if not self.linked_list.head:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        # new_node.next = self.linked_list.tail
        self.linked_list.tail.next = new_node
        self.linked_list.tail = new_node



queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
print(queue)