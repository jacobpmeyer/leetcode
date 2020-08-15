def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for i in range(n + 1)]
	ways[0] = 1
	for denom in denoms:
		for amount in range(1, n + 1):
			if amount >= denom:
				ways[amount] += ways[amount - denom]
	return ways[-1]