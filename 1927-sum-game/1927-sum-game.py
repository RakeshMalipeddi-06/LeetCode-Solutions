class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n=len(num)
        m=n//2
        left_sum=0
        left_q=0
        right_sum=0
        right_q=0

        for i in range(m):
            if num[i]=="?":
                left_q+=1
            else:
                left_sum+=int(num[i])
        for i in range(m,n):
            if num[i]=="?":
                right_q+=1
            else:
                right_sum+=int(num[i])
        
        if (left_q + right_q)%2==1:
            return True

        return left_sum - right_sum != 9 * (right_q - left_q) // 2   



        