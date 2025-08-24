class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs or "" in strs:
            return ""

        common_prefix = strs[0]
        
        for string in strs[1:]:
           while not string.startswith(common_prefix):
                common_prefix = common_prefix[:-1] 
                if not common_prefix:
                    return ""
        
        return common_prefix
        