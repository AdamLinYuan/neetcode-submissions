class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        p1, p2 = 0, 1
        profit = 0
        while p2 < len(prices) - 1:
            if prices[p1] < prices[p2]:
                temp = prices[p2] - prices[p1]
                profit = max(profit, temp)
                p2 += 1
            elif prices[p1] >= prices[p2]:
                p1 = p2
                p2 += 1

        temp = prices[p2] - prices[p1]
        profit = max(profit, temp)

        return profit
