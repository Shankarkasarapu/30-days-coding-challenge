class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        temp=[]
        seen=[False]*len(nums)
        nums.sort()

        def backt():
            if len(temp)==len(nums):
                res.append(temp[:])
                return
            for i in range(len(nums)):
                if seen[i]==True:
                    continue
                if i>0 and nums[i]==nums[i-1] and not seen[i-1]:
                    continue 
                seen[i]=True
                temp.append(nums[i])
                backt()
                temp.pop()
                seen[i]=False   

        backt()
        return res


