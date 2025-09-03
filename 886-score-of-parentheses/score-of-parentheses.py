class Solution(object):
    def scoreOfParentheses(self, s):
        
        stack =[]
        for i in s:
            if i=="(":
                stack.append(-1)
            else:
                if stack[-1]==-1:
                    stack.pop()
                    stack.append(1)
                else:
                    isum=0
                    while stack[-1]!=-1:
                        isum+=stack.pop()
                    stack.pop()
                    stack.append(isum*2)
        res=0
        while len(stack)>0:
            res+=stack.pop()

        return res


        