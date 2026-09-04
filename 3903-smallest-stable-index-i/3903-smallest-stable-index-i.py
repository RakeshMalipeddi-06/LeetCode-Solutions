class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            ans=max(nums[0:i+1])-min(nums[i:])

            if ans<=k:
                return i
                break
        
        return -1


        