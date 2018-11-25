class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        temp = 0
        result = 0
        A.sort()
        for n in A:
            result += max(temp - n, 0)
            temp = max(temp + 1, n + 1)
        
        return result
