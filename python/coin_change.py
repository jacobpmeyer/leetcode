class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = [float("inf") for amount in range(amount + 1)]
        minCoins[0] = 0
        for coin in coins:
            for amount in range(1, len(minCoins)):
                if coin <= amount:
                    minCoins[amount] = min(minCoins[amount], minCoins[amount - denmon] + 1)
        return minCoins[-1]

coins = [1, 2, 5]
amount = 11
s = Solution()
print(s.coinChange(coins, amount))