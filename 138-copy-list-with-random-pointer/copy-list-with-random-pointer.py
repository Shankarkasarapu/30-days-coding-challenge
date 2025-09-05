"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return head
        tail= head 
        while tail is not None:
            newnode = Node(tail.val)
            newnode.next=tail.next
            tail.next=newnode
            tail=tail.next.next

        tail= head 
        while tail:
            if tail.random:
                tail.next.random =tail.random.next
            tail=tail.next.next
        
        curr=head 
        newhead = head.next 
        newcurr = newhead
        while curr and newcurr:
            curr.next=newcurr.next
            curr=curr.next
            if curr:
                newcurr.next=curr.next
                newcurr=newcurr.next
        return newhead

    
