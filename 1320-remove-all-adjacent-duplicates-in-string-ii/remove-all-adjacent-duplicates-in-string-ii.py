class Solution(object):
    def removeDuplicates(self, s, k):
        if len(s)==1:
            return s
        stack=[]
        for i in s :
            if len(stack)==0 or i!=stack[-1][0]:
                temp=[i,1]
                stack.append(temp)
            elif i==stack[-1][0]:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
        
        ans=""
        for i in stack :
            ans+=i[0]*i[1]
        return ans