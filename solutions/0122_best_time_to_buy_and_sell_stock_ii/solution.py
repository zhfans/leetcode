class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = max_price = prices[0]
        profit = 0

        for price in prices:
            if price > max_price:
                max_price = price
            elif price < max_price:
                profit = profit + max_price - min_price
                min_price = max_price = price

        if max_price > min_price:
            profit = profit + max_price - min_price

        return profit


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
