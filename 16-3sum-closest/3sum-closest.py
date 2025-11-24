class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        ans=[]
        nums.sort()
        closest=float('inf')
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if abs(target-total) < abs(target-closest):
                    closest= total
                if total> target:
                    r-=1
                elif total< target:
                    l+=1
                else :
                    return total
        return closest
                
                
