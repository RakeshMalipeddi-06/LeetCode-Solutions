class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        h={}

        for ch in magazine:
            h[ch]=h.get(ch,0)+1
        
        for ch in ransomNote:
            if ch not in h:
                return False
            if h[ch]==0:
                return False
            
            h[ch]-=1
        
        return True
        