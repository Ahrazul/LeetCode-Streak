# Problem: Best time to buy and sell stocks
# Difficulty: Easy
# Runtime: 760 ms (Beats 50% of LeetCode users)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxp = max(profit,maxp)
            else:
                l = r
            r += 1
        return maxp
