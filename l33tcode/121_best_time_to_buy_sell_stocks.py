class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = 10000
        max_profit = 0
        
        for price in prices:
            min_price = min(price, min_price)
            if price > min_price:
                max_profit = max((price - min_price),max_profit)
        
        return max_profit