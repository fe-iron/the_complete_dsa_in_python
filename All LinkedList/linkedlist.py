class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def insert(self, value, pos=0) -> bool:
        new_node = Node(value)
        if pos < 0 or pos > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_head = self.head
            while pos >= 1:
                pos -= 1
                temp_head = temp_head.next
            
            new_node.next = temp_head.next
            temp_head.next = new_node
        self.length += 1
        return True
    
    def __str__(self) -> str:
        result = ''
        temp_head = self.head
        while temp_head is not None:
            result += str(temp_head.value)
            if temp_head.next is not None:
                result += " -> "
            temp_head = temp_head.next
        return result

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head1
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def remove_duplicates(self):
        if self.head is None:
            return
        node_values = set()  # set to store unique node values
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:  # duplicate found
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node

l1 = LinkedList()
l1.insert(10)
l1.insert(20)
l1.insert(30)
print(l1)

