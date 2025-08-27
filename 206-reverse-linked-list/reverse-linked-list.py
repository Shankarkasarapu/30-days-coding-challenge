# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None  # Initialize prev as None
        curr = head  # Start with curr at the head of the list

        while curr:
            temp = curr.next  
            curr.next = prev  
            prev = curr       
            curr = temp
        return prev
        