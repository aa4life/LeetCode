class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = float('inf')
        result = 0
        for p in prices:
            minprice = min(minprice, p)
            if p - minprice > result:
                result = p - minprice
        
        return result