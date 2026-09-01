class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=len(s)-1
        c=0

        while i>=0 and s[i]==" ":
            i=i-1
        
        while i>=0 and s[i]!=" ":
            c=c+1
            i=i-1
        
        return c
        