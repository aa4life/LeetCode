class Solution:
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        endletter = [0] * 26
        
        for c in S:
            endletter[ord(c) - ord('a')] = sum(endletter) + 1

        return sum(endletter) % (10 ** 9 + 7)