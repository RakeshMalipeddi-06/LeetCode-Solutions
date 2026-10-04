from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q=deque()
        rows=len(grid)
        cols=len(grid[0])
        fresh=0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        mins=0
        directions=[(0,-1),(-1,0),(0,1),(1,0)]
        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<rows and 0<=nc<cols:
                        if grid[nr][nc]==1:
                            grid[nr][nc]=2
                            fresh-=1
                            q.append((nr,nc))
            
            mins+=1
        
        if fresh>0:
            return -1
        
        return mins

        