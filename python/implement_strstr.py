# h is the length of the haystack, n is the length of the needle
# O((h - n)n) Time | O(1) Space
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, h = len(needle), len(haystack)
        if n == 0:
            return 0
        ph = 0
        while ph < h - n + 1:
            while ph < h - n + 1 and haystack[ph] != needle[0]:
                ph += 1
            pn = 0
            currLen = 0
            while ph < h and pn < n and haystack[ph] == needle[pn]:
                pn += 1
                currLen += 1
                ph += 1
            if currLen == n:
                return ph - currLen
            ph = ph - currLen + 1
        return -1