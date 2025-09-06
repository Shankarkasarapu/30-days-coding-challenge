class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        maxheap=[]
        for (x,y) in points:
            dist=-(x*x+y*y)
            heapq.heappush(maxheap,(dist,[x,y]))
            if len(maxheap)>k:
                heapq.heappop(maxheap)
        p=[p for i,p in maxheap]
        return p


        