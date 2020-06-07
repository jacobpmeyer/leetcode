
# O(nd) Time where n is n and d is the number of denominations | O(n) Space
def numberOfWaysToMakeChange(n, denoms):
	ways = [0 for amount in range(n + 1)]
	ways[0] = 1
	for denom in denoms:
		for amount in range(1, n + 1):
			if denom <= amount:
				ways[amount] += ways[amount - denom]
	return ways[n]


# {"denoms": [1, 5, 10, 25], "n": 5} | expected => 2 | my code => 5

print(numberOfWaysToMakeChange(5, [1, 5, 10, 25]))