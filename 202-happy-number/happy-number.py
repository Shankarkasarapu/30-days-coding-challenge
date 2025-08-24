class Solution(object):
    def sums(self ,n):
        sum=0
        for i in str(n):
            sum+=int(i)**2
        return sum
        
    def isHappy(self, n):

        s=set()
        while n!=1:
            if n in s:
                return False
            s.add(n)
            
            n=self.sums(n)
        return True


    
    
    