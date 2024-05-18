"""Remove Duplicates
Write a function to remove duplicates from an unsorted linked list.
Input 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5 
Output 1 -> 2 -> 3 -> 4 -> 5"""

from random import randint

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return self.value
    

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def __str__(self) -> str:
        value =  [str(x.value) for x in self]
        return " -> ".join(value)
    
    def __len__(self):
        curr = self.head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        return length
    
    def add(self, value):
        new_code = Node(value)
        if self.head is None:
            self.head = new_code
            self.tail = new_code
        else:
            self.tail.next = new_code
            self.tail = new_code
        return self.tail
    
    def generate(self, n, min_val=0, max_val=1000000):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_val, max_val))
        return self

    

l1 = LinkedList()
ll = l1.generate(10, 1, 3)
print(ll)
