class Solution:
    def backtrack(self, result,temp , nums , start ):
        result.append(temp[:])
        for i in range(start,len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            temp.append(nums[i])
            self.backtrack(result , temp , nums , i+1)
            temp.pop()
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []
        nums.sort()
        self.backtrack(result , temp , nums , 0)
        return result  
    