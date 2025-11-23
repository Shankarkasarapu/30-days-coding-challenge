class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        total= sum(nums)
        if total%3==0 :
            return total
        rem1_arr=[]
        rem2_arr=[]
        
        for i in nums:
            if i % 3 == 1:
                rem1_arr.append(i)
            if i % 3 ==2 :
                rem2_arr.append(i)
        rem1_arr.sort()
        rem2_arr.sort()
        rem=total%3
        for i in range(len(nums)):
            if rem==1:
                opt1 = total-rem1_arr[0] if rem1_arr else 0 
                opt2 = total-rem2_arr[0]-rem2_arr[1] if len(rem2_arr)>2 else 0
                return max(opt1, opt2)
            if rem==2:
                opt1 = total-rem2_arr[0] if rem2_arr else 0
                opt2 = total- rem1_arr[0]-rem1_arr[1] if len(rem1_arr)>=2 else 0
                return max(opt1, opt2)
