class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, reset = float("-inf"), float("-inf"), 0
            for price in prices:
                preSold = sold
                sold = held + prices[i]
                held = max(held, reset)
                reset = max(preSold, reset)
            return max(sold, reset)