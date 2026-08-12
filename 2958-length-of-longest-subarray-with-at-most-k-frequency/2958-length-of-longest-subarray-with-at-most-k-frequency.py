class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        h={}
        l=0
        ans=0
        for r in range(len(nums)):
            h[nums[r]]=h.get(nums[r],0)+1

            while h[nums[r]]>k:
                h[nums[l]]=h[nums[l]]-1
                l=l+1
            
            ans=max(ans,r-l+1)
        
        return ans