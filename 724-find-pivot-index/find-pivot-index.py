class Solution(object):
    def pivotIndex(self, nums):

        left_sum = 0 
        right_sum = 0 
        sum=0
        self.arr=[]
        for i in nums :
            sum+=i
            self.arr.append(sum)

        for i in range(0,len(nums)):
            if self.sums(0,i-1)==self.sums(i+1,len(nums)-1):
                return i
            else :
                continue
        return -1
    
    
    
    def sums(self, left, right):
        
        if left > right:
            return 0
        if left == 0:
            return self.arr[right]
        return self.arr[right] - self.arr[left - 1]

            
        