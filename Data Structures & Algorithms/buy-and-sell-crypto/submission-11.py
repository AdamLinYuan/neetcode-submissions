class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        p1, p2 = 0, 1
        profit = 0

        while p2 < len(prices):
            if prices[p1] < prices[p2]:
                profit = max(profit, prices[p2] - prices[p1])
                p2 += 1
            else:
                p1 = p2
                p2 += 1

        return profit
