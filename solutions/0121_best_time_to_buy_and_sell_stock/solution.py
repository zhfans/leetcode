class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        if n == 1:
            return 0

        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
