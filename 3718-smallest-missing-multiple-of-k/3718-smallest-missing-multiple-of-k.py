class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        n=len(nums)
        i=1*k
        while i in nums:
            i=i+k
        
        return i
        