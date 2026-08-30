class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        min_ind=nums.index(min(nums))
        max_ind=nums.index(max(nums))
        
        if min_ind>max_ind:
            min_ind,max_ind=max_ind,min_ind
        
        ans=min(max_ind + 1, n - min_ind, min_ind + 1 + (n - max_ind))
        return ans