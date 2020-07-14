class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}
        for char in s:
            first[char] = first.get(char, 0) + 1
        for char in t:
            second[char] = second.get(char, 0) + 1
        return first == second