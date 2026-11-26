class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections)<n-1:
            return -1
        count=0
        visited=set()
        g=[[] for _ in range(n)]

        for u,v in connections:
            g[u].append(v)
            g[v].append(u)
        
        def dfs(i):
            if i not in visited:
                visited.add(i)
            for nei in g[i]:
                if nei not in visited:
                    dfs(nei)
        
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)
        
        return count-1
        
        

        