class Solution(object):
    def arrayPairSum(self, nums):
        sum=0 
        sorte=sorted(nums)
        for i in range(0,len(sorte),2):
            sum+=sorte[i]
        return sum 