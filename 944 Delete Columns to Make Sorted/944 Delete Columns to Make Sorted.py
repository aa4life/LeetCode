class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result = 0
        for i in range(len(A[0])):
            for j in range(1, len(A)):
                if A[j][i] < A[j-1][i]:
                    result += 1
                    break;
        
        return result