class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = list(range(1, n - k))
        
        for i in range(k + 1):
            if i % 2 == 0:
                result.append(n - k + i//2)
            else:
                result.append(n - i//2)
        '''
        result = list(range(1, k+2))
        for i in range(1, k):
            temp = result.pop()
            result.insert(2*i - 1, temp)
        
        for i in range(k + 2, n+1):
            result.append(i)
        '''
        return result
