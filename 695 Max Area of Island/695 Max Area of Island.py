class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        def getarea(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + getarea(i - 1, j) + getarea(i, j + 1) + getarea(i + 1, j) + getarea(i, j - 1)
            return 0

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    max_area = max(max_area, getarea(i, j))
                    
        return max_area