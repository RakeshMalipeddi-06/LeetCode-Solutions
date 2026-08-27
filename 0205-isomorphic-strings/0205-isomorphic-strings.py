class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1={}
        t1={}

        for i in range(len(s)):
            if s[i] in s1 and s1[s[i]]!=t[i]:
                return False
            if t[i] in t1 and t1[t[i]]!=s[i]:
                return False
            
            s1[s[i]]=t[i]
            t1[t[i]]=s[i]
        
        return True
        