class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        
        result = 0
        for i in range(len(A)):
            result += A[i]*i
        
        suma = sum(A)
        temp = result
        for i in range(1, len(A)):
            temp = temp - suma + (len(A))*A[i-1]
            result = max(result, temp)
        
        return result