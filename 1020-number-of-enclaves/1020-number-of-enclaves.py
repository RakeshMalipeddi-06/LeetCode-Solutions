class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        row=len(grid)
        col=len(grid[0])
        d=([])
        
        def dfs(i,j):
            if i<0 or i>=row or j<0 or j>=col:
                return
            if grid[i][j]==0:
                return
            grid[i][j]=0
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    if i==0 or i==row-1 or j ==0 or j ==col-1:
                        dfs(i,j)

        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    count+=1      

        return count  