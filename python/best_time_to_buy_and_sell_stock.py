class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		profit = 0
		selling = 0
		for i in range(len(prices) - 1):
			currentDay = prices[i]
			nextDay = prices[i + 1]
			if not selling:
				if currentDay < nextDay:
					selling = currentDay
			else:
				if currentDay > nextDay:
					profit += currentDay - selling
					selling = 0	
			if i + 2 == len(prices) and selling:
				profit += nextDay - selling
				selling = 0
		return profit