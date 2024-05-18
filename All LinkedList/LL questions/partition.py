from LinkedList import LinkedList

def partition(ll, num):
    temp_node = ll.head
    ll.tail = ll.head
    while temp_node:
        next_node = temp_node.next
        temp_node.next = None
        if temp_node.value < num:
            temp_node.next = ll.head
            ll.head = temp_node
        else:
            ll.tail.next = temp_node
            ll.tail = temp_node
        temp_node = next_node
    if ll.tail.next is not None:
        ll.tail.next = None



l1 = LinkedList()
ll = l1.generate(10, min_val=10, max_val=20)
print(ll)
partition(ll, 15)
print(ll)