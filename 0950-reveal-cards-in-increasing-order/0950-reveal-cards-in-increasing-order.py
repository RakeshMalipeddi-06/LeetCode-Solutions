from collections import deque
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        q=deque(range(len(deck)))
        ans=[0]*len(deck)

        for card in deck:
            pos=q.popleft()
            ans[pos]=card

            if q:
                q.append(q.popleft())
        
        return ans
        