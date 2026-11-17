# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        q=deque([root])
        r=[]
        if root is None:
            return []
        rev=False
        while q:
            l=[]
            for i in range(len(q)):
                node=q.popleft()
                l.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            if rev:
                l.reverse()
            r.append(l)
            rev= not rev
        return r

            


        