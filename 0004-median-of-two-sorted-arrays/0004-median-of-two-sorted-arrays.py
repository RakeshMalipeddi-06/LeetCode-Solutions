class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i=0
        j=0
        m=len(nums1)
        n=len(nums2)
        merge=[]

        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                merge.append(nums1[i])
                i=i+1
            else:
                merge.append(nums2[j])
                j=j+1
        while i<m:
            merge.append(nums1[i])
            i=i+1
        while j<n:
            merge.append(nums2[j])
            j=j+1
        
        n=len(merge)

        if n%2==1:
            return merge[n//2]
        
        return (merge[n//2]+merge[n//2-1])/2.0