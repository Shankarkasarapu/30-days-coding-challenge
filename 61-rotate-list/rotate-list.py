# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k==0 :
            return head

        l =1
        tail=head
        while tail.next is not None:
            tail=tail.next
            l+=1
        k=k%l
        if k==0 :
            return head
        
        breakpoint=l-k-1
        temp = head 
        for i in range(breakpoint):
            temp=temp.next
        newhead=temp.next
        temp.next=None
        tail.next=head
        return newhead


