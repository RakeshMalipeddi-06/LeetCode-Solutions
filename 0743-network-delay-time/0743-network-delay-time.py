import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graphs={i:[] for i in range(1,n+1)}

        for u,v,w in times:
            graphs[u].append((v,w))
        
        dist=[float('inf')]*(n+1)
        dist[k]=0

        minheap=[(0,k)]

        while minheap:
            currdist,currnode=heapq.heappop(minheap)

            if currdist>dist[currnode]:
                continue
            
            for neigh,w in graphs[currnode]:
                newdist=w+currdist

                if newdist<dist[neigh]:
                    dist[neigh]=newdist

                    heapq.heappush(minheap,(newdist,neigh))
        
        if float('inf') in dist[1:]:
            return -1
        
        return max(dist[1:])