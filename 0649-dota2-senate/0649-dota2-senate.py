from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n=len(senate)
        q1=deque()
        q2=deque()
        for i in range(len(senate)):
            if senate[i]=="R":
                q1.append(i)
            else:
                q2.append(i)
        while q1 and q2:
            r=q1.popleft()
            d=q2.popleft()
            if r<d:
                q1.append(r+n)
            else:
                q2.append(d+n)
        
        if q1:
            return "Radiant"
        else:
            return "Dire"
