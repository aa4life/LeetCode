class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        maxnum = len(S)
        minnum = 0
        result = []
        for c in S:
            if c == 'I':
                result.append(minnum)
                minnum += 1
            else:
                result.append(maxnum)
                maxnum -= 1
        result.append(maxnum)
        
        return result