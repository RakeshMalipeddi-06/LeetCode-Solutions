class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        m=float('inf')

        for i in range(len(nums1)):
            if nums1[i]%2==1:
                m=min(m,nums1[i])
        if m==float('inf'):
            return True
        
        for j in nums1:
            if j%2==0 and j < m:
                return False

        return True 
        