class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        
        
        height = A[0]
        downhill = False
        uphill = False
        for n in A[1:]:
            if n == height:
                return False
            if n > height:
                uphill = True
                height = n
                if downhill:
                    return False
            if n < height:
                downhill = True
                height = n
                
        if not uphill or not downhill:
            return False
        return True
                