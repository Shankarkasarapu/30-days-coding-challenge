class Solution(object):
    def firstUniqChar(self, s):
        counter= {}
        for char in s :
            if char in counter:
                counter[char]+=1
            
            else :
                counter[char]=1

        for i in range(len(s)):
            if counter[s[i]]==1:
                return i
        return -1
        