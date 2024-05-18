"""
    Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1: 
Input: head = [1,2]
Output: [2,1]

Example 2: 
Input: head = []
Output: []

"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def reverseList(self, head):
     # Solution goes here
        if not head:
            return head
        prev = head
        current = head.next
        head.next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
             
        return prev