class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """

        n = len(bloomDay)

        # Impossible case
        if m * k > n:
            return -1

        def canmake(day):

            bq = 0
            flowers = 0

            for bloom in bloomDay:

                if bloom <= day:
                    flowers += 1

                    if flowers == k:
                        bq += 1
                        flowers = 0

                else:
                    flowers = 0

            return bq >= m


        # Binary Search on Answer
        l = min(bloomDay)
        h = max(bloomDay)

        while l <= h:

            mid = (l + h) // 2

            if canmake(mid):
                h = mid - 1

            else:
                l = mid + 1

        return l