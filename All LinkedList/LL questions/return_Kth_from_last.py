"""
return kth element from last 
"""

from LinkedList import LinkedList

def return_from_last(ll, n):
    slow = ll.head
    fast = ll.head
    for i in range(n):
        if fast is None:
            print("inside none")
            return None
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow


l1 = LinkedList()
ll = l1.generate(10, 1, 10)
print(ll)
print(return_from_last(ll, 7).value)