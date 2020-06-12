
# Memoized solution
# O(n) Time | O(n) Space where in is the dictionary being used for memoization
def getNthFib(n, seen = {1: 0, 2: 1}):
	if n in seen:
		return seen[n]
	else:
		seen[n] = getNthFib(n - 1, seen) + getNthFib(n - 2, seen)
		return seen[n]
	
# O(n) Time | O(1) Space
def getNthFib(n):
	lastTwo = [0, 1]
	counter = 3
	while counter <= n:
		newLast = lastTwo[0] + lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = newLast
		counter += 1
	return lastTwo[1] if n > 1 else lastTwo[0] 