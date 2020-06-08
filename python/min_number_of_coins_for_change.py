def minNumberOfCoinsForChange(n, denoms):
	coinNums = [float("inf") for amount in range(n + 1)]
	coinNums[0] = 0
	for denom in denoms:
		for amount in range(len(coinNums)):
			if denom <= amount:
				coinNums[amount] = min(coinNums[amount], coinNums[amount - denom] + 1)

	return coinNums[n] if coinNums[n] != float("inf") else -1