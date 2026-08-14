class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l=0
        h={}
        best=1
        curr=0

        for r in range(len(s)):
            h[s[r]]=h.get(s[r],0)+1
            while h[s[r]]>2:
                h[s[l]]-=1
                l=l+1
            curr = r-l+1
            best=max(best,curr)
        
        return best


        