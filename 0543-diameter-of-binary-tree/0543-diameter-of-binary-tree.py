# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.result=0
        def dia(node):
            if node is None:
                return 0
            
            l=dia(node.left)
            r=dia(node.right)

            self.result=max(self.result,l+r)
            return 1+max(l,r)
        
        dia(root)
        return self.result
        