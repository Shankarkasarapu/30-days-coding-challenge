class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans=0
        for i in range(len(number)):
            if number[i] == digit:
                t=number[:i]+number[i+1:]
                ans=max(ans,int(t))
        return str(ans)