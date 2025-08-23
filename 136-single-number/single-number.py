class Solution(object):
    def singleNumber(self, nums):
        hashmap= {}
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        for i in hashmap:
            if hashmap[i]==1:
                return i
        