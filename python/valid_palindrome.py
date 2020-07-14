class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        l = []
        for char in s:
            if char.lower() not in alpha:
                continue
            l.append(char)
        print(l)
        print(l[::-1])
        return l == l[::-1]

s = Solution()
print(s.isPalindrome("poo,54::::     p"))
print(s.isPalindrome("racecar"))