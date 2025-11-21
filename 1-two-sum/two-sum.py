class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i , v in enumerate(nums):
            res = seen.get(target-v)
            if res is not None :
                return i,res
            seen[v]=i
