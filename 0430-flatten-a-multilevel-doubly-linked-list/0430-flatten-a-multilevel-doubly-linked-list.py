"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curr=head
        while curr:
            if curr.child:
                nn=curr.next
                child_head=curr.child
                child_tail=curr.child

                while child_tail.next:
                    child_tail=child_tail.next

                curr.next=child_head
                child_head.prev=curr

                if nn:
                    nn.prev=child_tail
                    child_tail.next=nn
                
                curr.child=None
            
            curr=curr.next
        
        return head
        