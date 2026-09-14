# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        seen=set()
        curr=head
        prev=None

        while curr:
            if curr.val in seen:
                prev.next=curr.next
            else:
                prev=curr
            seen.add(curr.val)
            curr=curr.next
        
        return head

            


        