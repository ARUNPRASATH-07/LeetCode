class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
    
        for price in prices:
        # Update the lowest price we've seen so far
            if price < min_price:
                min_price = price
        # Check if selling today gives a better profit than what we've seen before
            elif price - min_price > max_profit:
                max_profit = price - min_price
            
        return max_profit