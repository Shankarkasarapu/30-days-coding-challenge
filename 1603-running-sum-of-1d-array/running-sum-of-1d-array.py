class Solution(object):
    def runningSum(self, nums):
        arr=[]
        sum=0
        for i in nums:
            sum+=i
            arr.append(sum)
        return arr