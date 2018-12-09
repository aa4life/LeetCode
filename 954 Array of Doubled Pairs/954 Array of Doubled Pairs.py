import collections

class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        num0 = 0
        minus = 0
        for i in range(len(A)):
            if A[i] == 0:
                num0 += 1
            if A[i] < 0:
                A[i] = -1 * A[i]
                minus += 1
        if minus % 2 != 0 or num0 % 2 != 0:
            return False
        
        A.sort()
        count = collections.Counter(A)
        for k in sorted(count.keys()):
            if count[k] > count[2*k]:
                return False
            count[2*k] -= count[k]
        return True
                