class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        ans=1
        if k%2==0 or k%5==0 : return -1
        length=0
        while True:
            length+=1
            if ans%k==0:
                return length
            if length>k: break
            ans=(ans*10+1)
        