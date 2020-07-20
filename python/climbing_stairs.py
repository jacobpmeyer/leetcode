class Solution:
    def climbStairs(self, n: int) -> int:
        def stairHelper(num, mem):
            if num <= 2:
                return num
            if num in mem:
                return mem[num]
            mem[num] = stairHelper(num - 1, mem) + stairHelper(num - 2, mem)
            return mem[num]
        mem = {}
        return stairHelper(n, mem)