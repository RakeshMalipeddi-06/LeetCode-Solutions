class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h={}
        ans=-1
        

        n=len(nums)
        for i in range(n-k+1):
            unique=set(nums[i:i+k])

            for i in unique:
                h[i]=h.get(i,0)+1
        
        for i in h:
            if h[i]==1:
                ans=max(ans,i)
        
        return ans
        
        



        