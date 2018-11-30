import collections

class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        c = collections.Counter(str(N))
        for i in range(32):
            if c == collections.Counter(str(1 << i)):
                return True
        return False