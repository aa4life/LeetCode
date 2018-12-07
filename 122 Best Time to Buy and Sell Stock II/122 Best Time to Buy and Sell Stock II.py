class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        cash = 0
        hold = -prices[0]
        for p in prices[1:]:
            cash, hold = max( cash, hold + p), max( hold, cash - p)
        
        return cash