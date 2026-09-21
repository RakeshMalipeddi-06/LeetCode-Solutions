class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        h={}
        for num in nums2:
            while stack and stack[-1]<num:
                small=stack.pop()
                h[small]=num
            stack.append(num)
        
        for i in stack:
            h[i]=-1
        
        return [h[num] for num in nums1]
        