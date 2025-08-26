class Solution(object):
    def largestNumber(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if str(nums[i])+str(nums[j])<str(nums[j])+str(nums[i]):
                    nums[i],nums[j]=nums[j],nums[i]
        
        s=int(''.join(map(str,nums)))
        return str(s)


        