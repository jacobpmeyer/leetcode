
# O(n) Time where n is the length of prices
# O(1) Space
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		# We are going to use i to keep track of our place in prices
		i = 0
		# We set valley and peak to be the first value of prices
		valley = prices[0]
		peak = prices[0]
		# Keep track of our max profit
		total = 0
		# Now we iterate over prices. We stop at the second to last position
		# because will iterate to the last one with our nested while loops
		while i < len(prices) - 1:
			# We iterate until we know the value is strictly less that it's next val
			while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
				i += 1
			# Set valley equal to where we stopped
			valley = prices[i]
			# Iterate until we find a value that is strictly more that its next value
			while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
				i += 1
			# Set the peak because we know it is
			peak = prices[i]
			# Add to the total (Sell the stock)
			total += peak - valley
		# After a single pass through, we return the total
		return total