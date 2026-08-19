class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """

        rows={}
        for row,reserved in reservedSeats :
            if row not in rows:
                rows[row]=set()
            rows[row].add(reserved)
        

        ans=n*2

        for seats in rows.values():

            left=True
            for seat in [2,3,4,5]:
                if seat in seats:
                    left=False
                    break
            mid=True
            for seat in [4,5,6,7]:
                if seat in seats:
                    mid=False
                    break
            right=True
            for seat in [6,7,8,9]:
                if seat in seats:
                    right=False
                    break
            
            if left and right:
                continue
            elif left or mid or right :
                ans-=1
            else:
                ans-=2
        return ans
            
