"""Insert into a Sorted Circular Linked List
Write a function to insert a new node into a sorted circular linked list."""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node


    def insert_into_sorted(self, data):
        # TODO
        new_code = Node(data)
        if not self.head:
            self.head = new_code
            new_code.next = new_code
        elif data <= self.head.data:
            self.prepend(data)
        else:
            temp = self.head
            while temp is not self.head and temp.next.data < data:
                temp = temp.next
            new_code.next = temp.next
            temp.next = new_code