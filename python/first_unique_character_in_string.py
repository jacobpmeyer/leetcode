class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        for i, char in enumerate(s):
            chars[char] = chars.get(char, 0) + 1
        for i, char in enumerate(s):
            if chars[char] == 1:
                return i
        return -1