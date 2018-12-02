import itertools

class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        result = ""
        temp = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            if h1*10 + h2 < 24 and m1 < 6:
                time = (h1*10 + h2) * 100 + m1 * 10 + m2
                if time > temp:
                    temp = time
                    result = str(h1) + str(h2) + ':' + str(m1) + str(m2)
        
        return result