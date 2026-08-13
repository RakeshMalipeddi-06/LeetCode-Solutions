class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """

        rows=len(mat)
        cols=len(mat[0])

        l=0
        r=cols-1

        while l<=r:
            m=(l+r)//2

            max_row=0
            for i in range(rows):
                if mat[i][m]>mat[max_row][m]:
                    max_row=i
            
            left=mat[max_row][m-1] if m>0 else -1
            right=mat[max_row][m+1] if m<cols-1 else -1

            if mat[max_row][m]>left and mat[max_row][m]>right:
                return [max_row,m]
            
            if mat[max_row][m]<left:
                r=m-1
            else:
                l=m+1
            

        