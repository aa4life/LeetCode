class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash = 0
        hold = -prices[0]
        for p in prices[1:]:
            cash, hold = max( cash, hold + p - fee), max( hold, cash - p)
        
        return cash