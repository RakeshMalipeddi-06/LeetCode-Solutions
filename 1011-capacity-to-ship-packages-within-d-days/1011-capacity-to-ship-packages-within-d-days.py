class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        l=max(weights)
        h=sum(weights)

        while l<=h:
            m=(l+h)//2
            req_days=1
            total_weights=0
            for w in weights:
                if total_weights+w<=m:
                    total_weights+=w
                else:
                    req_days+=1
                    total_weights=w
            
            if req_days<=days:
                h=m-1
            else:
                l=m+1
        
        return l