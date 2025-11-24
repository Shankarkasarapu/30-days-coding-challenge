class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ans=[]
        # nums.sort()
        # for i in range(len(nums)):
        #     if i>0 and nums[i]==nums[i-1]:
        #         continue
        #     left,right=i+1,len(nums)-1
        #     while left<right:
        #         total=nums[left]+nums[right]+nums[i]
        #         if total==0:
        #             ans.append([nums[i],nums[left],nums[right]])
        #             while left<right and nums[left] == nums[left+1]:
        #                 left+=1 
        #             while left<right and nums[right]== nums[right-1]:
        #                 right-=1
        #             left+=1
        #             right-=1
        #         elif total>0:
        #             right-=1
        #         else : left+=1
                
        # return ans
        n=len(nums)
        nums.sort()
        ans=[]
        for i in range(n-1):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            l=i+1
            r=n-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if total==0:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif total>0:
                    r-=1
                else:
                    l+=1
        return ans