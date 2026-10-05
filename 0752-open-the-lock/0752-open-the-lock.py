from collections import deque
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        dead=set(deadends)
        if "0000" in dead:
            return -1
        q=deque(["0000"])
        visited=set(["0000"])
        moves=0

        while q:
            for _ in range(len(q)):
                curr=q.popleft()

                if curr==target:
                    return moves
                
                for i in range(4):
                    digit=int(curr[i])

                    for change in [-1,1]:
                        new_digit=(digit+change)%10

                        new_state=curr[:i]+str(new_digit)+curr[i+1:]

                        if new_state in dead:
                            continue
                        if new_state in visited:
                            continue
                        q.append(new_state)
                        visited.add(new_state)
                
            moves+=1
        
        return -1

        