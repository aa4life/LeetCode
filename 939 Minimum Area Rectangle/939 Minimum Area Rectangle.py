class Solution:
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        seen = set()
        result = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    temp = abs(x1 - x2) * abs(y1 - y2)
                    if temp < result:
                        result = temp
            seen.add((x1, y1))
        
        if result == float('inf'):
            result = 0
        
        return result