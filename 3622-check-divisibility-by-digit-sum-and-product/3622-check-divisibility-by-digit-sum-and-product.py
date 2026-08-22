class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=0
        p=1
        temp=n
        while temp>0:
            digit=temp%10
            temp=temp//10

            s=s+digit
            p=p*digit
        total=s+p

        if n%total==0:
            return True
        
        return n%total==0
        