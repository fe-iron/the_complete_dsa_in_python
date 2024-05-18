class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None


class Stack:
    def __init__(self) -> None:
        self.linked_list = LinkedList()

    def __iter__(self):
        curNode = self.linked_list.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self) -> str:
        if not self.linked_list.head:
            return ''
        result = ''
        result = [str(x.value) for x in self]
        # temp_head = self.linked_list.head
        # while temp_head:
        #     result += str(temp_head.value)
        #     temp_head = temp_head.next
        return " -> ".join(result)
    
    def push(self, value):
        new_node = Node(value)
        if not self.linked_list.head:
            self.linked_list.head = new_node
        else:
            new_node.next = self.linked_list.head
            self.linked_list.head = new_node


    def isEmpty(self):
        if self.linked_list.head:
            return False
        return True

    def pop(self):
        if self.isEmpty():
            return "There is no element in Stack"
        ret_val = self.linked_list.head.value
        self.linked_list.head = self.linked_list.head.next
        return ret_val
    
    def peek(self):
        if not self.linked_list.head:
            return None
        return self.linked_list.head.value
    
    def delete(self):
        self.linked_list.head = None



s1 = Stack()
print(s1)
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.isEmpty()
s1.peek()
s1.pop()
print(s1)
s1.delete()