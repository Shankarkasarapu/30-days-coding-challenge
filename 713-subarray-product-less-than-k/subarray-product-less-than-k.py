import math
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        res=0
        prod=1
        left=0
        n=len(nums)
        for i in range(n):
            prod*=nums[i]
            while prod>=k:
                prod/=nums[left]
                left+=1
            res+=i-left+1

        return res


