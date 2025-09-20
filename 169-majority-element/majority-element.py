class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hasmap = {}
        for i in nums:
            if i not in hasmap:
                hasmap[i]=1
            hasmap[i]+=1
        return max(hasmap,key=hasmap.get)