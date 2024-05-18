"""
    Remove Duplicates
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well. 

Example 1:

Input: head = [1,1,2]
Output: [1,2]
Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        # TODO
        temp_node = head
        my_set = {}
        while temp_node is not None:
            if my_set.get(temp_node.val):
                prev.next = temp_node.next
            else:
                my_set[temp_node.val] = 1
                prev = temp_node
            temp_node = temp_node.next
        
        return head
