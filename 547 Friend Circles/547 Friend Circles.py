class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        num = len(M)
        checked = set()
        
        def check(i):
            checked.add(i)
            for j in range(num):
                if M[i][j] == 1 and j not in checked:
                    check(j)
        
        result = 0
        for i in range(num):
            if i not in checked:
                check(i)
                result += 1
                
        return result