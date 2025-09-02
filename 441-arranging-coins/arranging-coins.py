class Solution(object):
    def arrangeCoins(self, n):
        left , right,ans=0,n,0
        while left<=right:
            mid=(left+right)//2
            coins_needed=mid*(mid+1)/2
            if coins_needed>n:
                right=mid-1
            else :
                ans=mid
                left=mid+1
            
        return ans