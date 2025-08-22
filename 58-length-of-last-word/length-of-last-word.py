class Solution(object):
    def lengthOfLastWord(self, s):
        arr =s.split()
        return len(arr[len(arr)-1])
      