class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minProf = float("inf")
        for i in range(len(prices)):
            if prices[i] < minProf:
                minProf = prices[i]
            elif prices[i] - minProf > maxProf:
                maxProf = prices[i] - minProf
        return maxProf