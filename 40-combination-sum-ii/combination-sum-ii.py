class Solution:
    def backtrack(self, result,temp , nums , start ,target):
        if sum(temp)==target:
            result.append(temp[:])
        if sum(temp)>target:
            return 
        for i in range(start,len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            temp.append(nums[i])
            self.backtrack(result , temp , nums , i+1 ,target)
            temp.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        temp = []
        candidates.sort()
        self.backtrack(result , temp , candidates , 0 ,target)
        return result