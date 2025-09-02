class Solution(object):
    def shipWithinDays(self, weights, days):
        mincap = max(weights)
        maxcap = sum(weights)
        while mincap<maxcap :
            mid=(mincap+maxcap)/2
            D,curr_sum=1,0
            for w in weights :
                if w+curr_sum>mid:
                    D+=1
                    curr_sum=0
                curr_sum+=w
            if D>days :
                mincap=mid+1
            else:
                maxcap=mid
        return mincap
            