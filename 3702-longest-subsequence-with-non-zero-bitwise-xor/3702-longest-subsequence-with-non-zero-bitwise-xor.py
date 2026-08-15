class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        xor=0
        nonzero=False
        n=len(nums)

        for i in nums:
            xor^=i

            if i!=0:
                nonzero=True

        if xor!=0:
            return n
        
        if nonzero:
            return n-1
        
        return 0



        