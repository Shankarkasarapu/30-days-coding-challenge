class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new =[0]*2*len(nums)
        for i in range(len(nums)):
            new[i]=nums[i]
            new[i+len(nums)]= nums[i]
        return new