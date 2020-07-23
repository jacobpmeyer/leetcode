def getNthFib(n, memo = {}):
    if n <= 2:
		return n - 1
	if n in memo:
		return memo[n]
	memo[n - 1] = getNthFib(n - 1, memo)
	memo[n - 2] = getNthFib(n - 2, memo)
	return memo[n - 1] + memo[n - 2]