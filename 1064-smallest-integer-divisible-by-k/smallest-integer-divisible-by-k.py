class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 or k%5==0 : return -1
        rem=0
        length=0
        while True:
            length+=1
            rem=((rem*10)+1)%k
            if rem==0:
                return length
            if length >k : break

        return -1