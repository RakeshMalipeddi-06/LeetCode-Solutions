class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        commas=1
        power=1000

        while power<=n:
            c=n-power+1
            ans=ans+commas*c

            power=power*1000
            c0mmas=commas+1
        
        return ans

        