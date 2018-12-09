class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def checkorder(A, B):
            for idx in range(min(len(A),len(B))):
                if order.index(A[idx]) < order.index(B[idx]):
                    return True
                if order.index(A[idx]) > order.index(B[idx]):
                    return False
            if len(B) < len(A):
                return False
            return True
        
        for idx in range(1,len(words)):
            if not checkorder(words[idx-1], words[idx]):
                return False
        return True