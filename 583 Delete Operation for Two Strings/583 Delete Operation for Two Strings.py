class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def LCS(s1,s2):
            if not s1 or not s2:
                return 0
            if s1[-1] == s2[-1]:
                return LCS(s1[:-1], s2[:-1]) + 1
            return max(LCS(s1[:-1], s2), LCS(s1, s2[:-1]))
    
        def lcs(s1, s2):
            res = [''] * (len(s1) + 1)
            for i in range(len(res)):
                res[i] = [''] * (len(s2) + 1)

            for is1 in range(len(s1)):
                for is2 in range(len(s2)):
                    if s1[is1] == s2[is2]:
                        res[is1 + 1][is2 + 1] = res[is1][is2] + s1[is1]
                    elif len(res[is1 + 1][is2]) > len(res[is1][is2 + 1]):
                        res[is1 + 1][is2 + 1] = res[is1 + 1][is2]
                    else:
                        res[is1 + 1][is2 + 1] = res[is1][is2 + 1]
    
            return res[len(s1)][len(s2)]

        result = len(lcs(word1, word2))
        return (len(word1) - result) + (len(word2) - result)