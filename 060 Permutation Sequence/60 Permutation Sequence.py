class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numberstr = []
        for i in range(n):
            numberstr.append(str(i+1))
        factorial = [1]
        for i in range(2, n):
            factorial.append(factorial[i-2]*i)
            
        result = ""
        for i in range(n-1):
            index = (k-1)//factorial[-1-i]
            k = k%factorial[-1-i]
            result += numberstr.pop(index)
            
        
        if len(result) < n:
            result += numberstr[0]
        
        return result

        