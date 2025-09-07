from array import array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter=0
        for i in range(len(nums)):
            if i <len(nums)-1 and nums[i]==nums[i+1]:
                continue
            else :
                nums[counter]=nums[i]
                counter+=1  
        return counter
                    
        