def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for x in range(n + 1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, len(ways)):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
	print(ways)
    return ways[n]