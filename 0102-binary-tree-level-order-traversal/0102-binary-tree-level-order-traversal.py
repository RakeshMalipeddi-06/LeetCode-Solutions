
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []

        q = deque([root])
        result = []

        while q:
            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            result.append(level)

        return result


        