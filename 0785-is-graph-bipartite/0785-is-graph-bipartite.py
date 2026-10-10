from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n=len(graph)
        color=[-1]*n
        for start in range(n):
            if color[start]!=-1:
                continue
            
            q=deque([start])
            color[start]=0
            while q:
                curr=q.popleft()

                for nei in graph[curr]:
                    if color[nei]==-1:
                        color[nei]=1-color[curr]
                        q.append(nei)
                    elif color[curr]==color[nei]:
                        return False
        
        return True

        