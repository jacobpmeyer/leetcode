def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for x in range(n + 1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[-1] 

test = {"denoms": [2, 4], "n": 7}
print(numberOfWaysToMakeChange(test["n"], test["denoms"]))