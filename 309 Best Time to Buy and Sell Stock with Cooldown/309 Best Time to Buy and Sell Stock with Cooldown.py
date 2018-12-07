class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1:
            return 0
        
        cash = 0
        hold = -prices[0]
        cooldown = -prices[0]
        for p in prices[1:]:
            cash, cooldown, hold= max(cash, cooldown), hold + p, max(hold, cash - p)
        
        return max(cash, cooldown)