# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def mirror(left,right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val!=right.val:
                return False
            
            i=mirror(left.left,right.right)
            o=mirror(left.right,right.left)

            return i and o
        
        return mirror(root.left,root.right) if root else True
        