class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        held = -1
        profit = 0
        for i in range(len(prices)):
            if held >= 0 and prices[i - 1] < prices[i]:
                profit += prices[i] - held
                held = -1
            if i < len(prices) - 1 and prices[i + 1] > prices[i]:
                held = prices[i]
        return profit