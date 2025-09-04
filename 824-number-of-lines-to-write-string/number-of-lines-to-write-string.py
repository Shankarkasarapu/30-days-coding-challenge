class Solution(object):
    def numberOfLines(self, widths, s):
        sum,c=0,0
        for i in range(len(s)):
            char_width = widths[ord(s[i]) - ord('a')]
            if sum + char_width>100:
                c+=1
                sum=0
            sum+=char_width
        return [c+1,sum]


