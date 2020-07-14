class Solution:
    def reverse(self, x: int) -> int:
        positive = x >= 0
        answer = 0
        if not positive:
            x += -(x) * 2
        while x > 9:
            answer = (10 * answer) + (x % 10)
            x = x // 10
        answer = (10 * answer) + (x % 10)
        if not positive:
            answer = -(answer)
        if answer > 2**31 - 1 or answer < -2**31:
            return 0
        else:
            return answer