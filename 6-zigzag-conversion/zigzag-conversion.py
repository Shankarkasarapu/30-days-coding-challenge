class Solution(object):
    def convert(self, s, numRows):
        if numRows==1:
            return s
        state=False
        res=['']*min(numRows,len(s))
        currentrow=0

        for char in s:
            res[currentrow]+=char

            if currentrow==0:
                state=True
            elif currentrow==numRows-1:
                state=False
            
            if state:
                currentrow+=1
            else:
                currentrow-=1
        
        op=''.join(res)
        return op