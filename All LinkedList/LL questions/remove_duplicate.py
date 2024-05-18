from LinkedList import LinkedList

def remove_duplicates(ll):
    # TODO
    if not ll.head:
        return
    temp_node = ll.head
    temp_list = []
    prev = None
    while temp_node:
        if temp_node.value not in temp_list:
            print(temp_node.value)
            temp_list.append(temp_node.value)
            prev = temp_node
        else:
            if temp_node.next:
                if temp_node.next.value not in temp_list:
                    prev.next = temp_node.next
                    prev = temp_node
                    print("skipping ",temp_node.value)
                else:
                    print("skipping next ",temp_node.value)
            else:
                prev.next = None
        temp_node = temp_node.next
    ll.tail = prev
    return ll.head

    

l1 = LinkedList()
ll = l1.generate(10, 1, 3)
print(ll)
new_ll = remove_duplicates(ll)
print(new_ll)