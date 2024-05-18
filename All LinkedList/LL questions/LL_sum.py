from LinkedList import LinkedList

def sum_linked_list(llA, llB):
    l1 = llA.head
    l2 = llB.head
    carry = 0
    ll = LinkedList()
    while l1 or l2:
        result = carry
        if l1:
            result += l1.value
            l1 = l1.next
        if l2:
            result += l2.value
            l2 = l2.next
        ll.add(int(result % 10))
        carry = result / 10
    return ll


l1 = LinkedList()
l1 = l1.generate(5, 1, 3)
print(l1)
l2 = LinkedList()
l2 = l2.generate(5, 5, 10)
print(l2)
print(sum_linked_list(l1, l2))