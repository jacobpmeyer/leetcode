# O(n) Time | O(n) Space where n is the length of the string
# Bad Bad Poopie Solution
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

# O(n) Time | O(1) Space where n is the length of the input string
# The better solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if i < j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

s = Solution()
print(s.isPalindrome("poo,54::::     p"))
print(s.isPalindrome("r3aceca3r"))