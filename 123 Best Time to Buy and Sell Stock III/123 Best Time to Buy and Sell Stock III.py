class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        sold1 = 0
        sold2 = 0
        hold1 = -float('inf')
        hold2 = -float('inf')
        for p in prices:
            sold1, sold2, hold1, hold2 = max(sold1, hold1 + p), max(sold2, hold2 + p), max(hold1, 0 - p), max(hold2, sold1 - p)
        
        return sold2