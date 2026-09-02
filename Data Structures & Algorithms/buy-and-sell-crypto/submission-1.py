class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for buy in range(len(prices)-1):
            for sell in range(buy+1, len(prices)):
                max_profit = max(max_profit, prices[sell]-prices[buy])
        return max_profit
        