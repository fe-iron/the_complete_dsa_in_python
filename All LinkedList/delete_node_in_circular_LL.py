"""
    Delete a Node from a Circular Singly Linked List
Implement a method in the CircularLinkedList class to delete a node by value.
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
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def delete_by_value(self, value):
        # TODO
        # dummy = Node(-1)
        # prev = dummy.next
        if self.length == 0:
            return False
        if self.length == 1 and self.head.value == value:
            self.head = None
            self.tail = None
            self.length -= 1
            return True
        temp_node = self.head
        prev = None
        while temp_node:
            if temp_node.value == value:
                if temp_node == self.head:
                    self.head = temp_node.next
                    self.tail.next = self.head
                    # prev.next = self.head
                    # self.tail = prev
                else:
                    prev.next = temp_node.next
                    if temp_node == self.tail:
                        self.tail = prev
                self.length -= 1
                return True
            prev = temp_node
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return False
           