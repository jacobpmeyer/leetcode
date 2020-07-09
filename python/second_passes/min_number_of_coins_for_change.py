# Given an array of positive integers representing coin denominations and a
# single non-negative integer n representing a target amount of money, write a
# function that returns the smallest number of coins needed to make change for
# that target amount using the given coin denominations.

# If it is impossible to make change for the target amount, return -1

# Note that an unlimited amount  of coins is at your disposal.

def minNumberOfCoinsForChange(n, denoms):
    amounts = [float("inf") for x in range(n + 1)]
    amounts[0] = 0
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                amounts[amount] = min(
                    amounts[amount], amounts[amount - denom] + 1
                )
    return amounts[-1] if amounts[-1] != float("inf") else -1

n = 7
denoms = [1, 5, 10]

print(minNumberOfCoinsForChange(n, denoms)) # => 3