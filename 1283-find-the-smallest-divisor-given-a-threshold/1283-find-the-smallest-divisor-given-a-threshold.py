class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        l=1
        h=max(nums)
    
        while l<=h:
            m=(l+h)//2
            total=0
            for n in nums:
                total+=(n+m-1)//m
            
            if total<=threshold:
                h=m-1
            else:
                l=m+1
        
        return l
        