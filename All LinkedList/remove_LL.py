"""
    Remove Linked List Elements
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:

Input: head = [], val = 1
Output: []

Example 2:

Input: head = [7,7,7,7], val = 7
Output: []

"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        # TODO
        temp_node = ListNode(-1)
        temp_node.next = head
        prev = temp_node
        current = head
        while current is not None:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return temp_node.next
