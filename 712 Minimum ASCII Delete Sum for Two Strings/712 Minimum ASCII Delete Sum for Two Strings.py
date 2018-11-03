class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        def lcs(s1, s2):
            res = [0] * (len(s1) + 1)
            for i in range(len(res)):
                res[i] = [0] * (len(s2) + 1)
            
            for is1 in range(len(s1)):
                for is2 in range(len(s2)):
                    if s1[is1] == s2[is2]:
                        res[is1+1][is2+1] = res[is1][is2] + ord(s1[is1])
                    elif res[is1+1][is2] > res[is1][is2+1]:
                        res[is1+1][is2+1] = res[is1+1][is2]
                    else:
                        res[is1+1][is2+1] = res[is1][is2+1]
            
            return res[len(s1)][len(s2)]
        
        sums1 = 0
        sums2 = 0
        for c in s1:
            sums1 += ord(c)
        for c in s2:
            sums2 += ord(c)
        
        subsum = lcs(s1,s2)
        
        return sums1 + sums2 - 2 * subsum