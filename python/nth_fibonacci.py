
# Memoized solution
# O(n) Time | O(n) Space where in is the dictionary being used for memoization
def getNthFib(n, seen = {1: 0, 2: 1}):
	if n in seen:
		return seen[n]
	else:
		seen[n] = getNthFib(n - 1, seen) + getNthFib(n - 2, seen)
		return seen[n]
	
