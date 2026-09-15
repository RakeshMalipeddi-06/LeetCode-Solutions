# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        prevgp=dummy

        while True:

            kth=prevgp

            for i in range(k):
                kth=kth.next

                if kth is None:
                    return dummy.next
            
            nxtgp=kth.next

            prev=nxtgp
            curr=prevgp.next

            while curr!=nxtgp:
                nxtnode=curr.next
                curr.next=prev
                prev=curr
                curr=nxtnode
            oldstart=prevgp.next
            prevgp.next=kth

            prevgp=oldstart

        



        

        
        