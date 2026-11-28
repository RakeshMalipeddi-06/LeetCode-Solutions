class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        adj=[[] for _ in range(26)]

        for eq in equations:
            if eq[1]=="=":
                u=ord(eq[0])-ord('a')
                v=ord(eq[3])-ord('a')

                adj[u].append(v)
                adj[v].append(u)
        component=0
        visited=[-1]*26
        def dfs(node):
            visited[node]=component
            for nei in adj[node]:
                if visited[nei]==-1:
                    dfs(nei)
        
        for node in range(26):
            if visited[node]==-1:
                dfs(node)
                component+=1
        
        for eq in equations:
            if eq[1]=="!":
                u=ord(eq[0])-ord('a')
                v=ord(eq[3])-ord('a')

                if visited[u]==visited[v]:
                    return False
        
        return True
        

        