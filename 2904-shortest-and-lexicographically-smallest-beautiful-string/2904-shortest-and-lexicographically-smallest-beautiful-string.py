class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l=0
        c=0
        best=""
        for r in range(len(s)):
            if s[r]=="1":
                c=c+1
            while c>k:
                if s[l]=="1":
                    c=c-1
                l=l+1
            if c==k:
                while s[l]=="0":
                    l=l+1
                
                ans=s[l:r+1]

                if best=="" or len(ans)<len(best):
                    best=ans
                elif len(ans)==len(best) and ans<best:
                    best=ans
        
        return best 

                
                

        