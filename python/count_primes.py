class Solution:
    def countPrimes(self, n: int) -> int:
        h = {}
        for i in range(2, n):
            h[i] = True
        
        count = 0
        for key in h:
            if h[key] is True:
                count += 1
                multiplier = 2
                while (key * multiplier) < n:
                    h[key * multiplier] = False
                    multiplier += 1
        return count