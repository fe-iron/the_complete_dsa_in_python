"""
    Implement a Circular Singly Linked List
Create a circular singly linked list with methods to insert a new node at the beginning, end, and print  to display the list.

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class CSLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        # TODO
        temp_head = self.head
        result = ''
        while temp_head:
            result += str(temp_head.value)
            temp_head = temp_head.next
            if temp_head == self.head:
                break
            result += (" -> ")
        return result
    
    
    def append(self, value):
        # TODO
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    
    def prepend(self, value):
        # TODO
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1


