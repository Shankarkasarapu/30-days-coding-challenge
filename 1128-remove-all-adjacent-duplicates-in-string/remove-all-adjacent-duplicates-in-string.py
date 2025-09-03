class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        for i in s :
            if len(stack)==0 or stack[-1]!=i:
                stack.append(i)
            elif stack[-1]==i:
                stack.pop()
        return "".join(stack)