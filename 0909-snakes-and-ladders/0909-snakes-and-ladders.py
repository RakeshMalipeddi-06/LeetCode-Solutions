from collections import deque
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n=len(board)
        target=n*n
        start=1
        q=deque([1])
        visited={1}
        rolls=0

        while q:
            for _ in range(len(q)):
                curr=q.popleft()
                if curr==target:
                    return rolls
                
                for d in range(1,7):
                    nxt=curr+d
                    if nxt> target:
                        break
                    
                    Q=(nxt-1)//n
                    R=(nxt-1)%n

                    r=n-1-Q
                    if Q%2==0:
                        c=R
                    else:
                        c=n-1-R

                    if board[r][c]==-1:
                        destination=nxt
                    else:
                        destination=board[r][c]
                    
                    if destination not in visited:
                        visited.add(destination)
                        q.append(destination)
            rolls+=1
        return -1


        