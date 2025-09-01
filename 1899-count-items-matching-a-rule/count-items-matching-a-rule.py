class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        type=[]
        color=[]
        name=[]
        for i in items:
            type.append(i[0])
            color.append(i[1])
            name.append(i[2])
        if ruleKey == "color":
            s=color.count(ruleValue)
            return s 
        elif ruleKey == "type":
            s=type.count(ruleValue)
            return s  
        elif ruleKey == "name":
            s=name.count(ruleValue)
            return s  
        