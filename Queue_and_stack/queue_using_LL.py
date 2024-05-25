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

    def isEmpty(self):
        if not self.linked_list.head:
            return True
        return False
    
    def dequeue(self):
        if self.isEmpty():
            return "there is no element"
        ele = self.linked_list.head.value
        if self.linked_list.head == self.linked_list.tail:
            self.linked_list.head = None
            self.linked_list.tail = None
        else:
            self.linked_list.head = self.linked_list.head.next
        return ele

    def peek(self):
        if self.isEmpty():
            return "there is no element"
        return self.linked_list.head.value
    
    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
print(queue)
print(queue.dequeue())
print(queue)
queue.enqueue(50)
queue.peek()