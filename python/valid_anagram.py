# O(s + t) Time | O(s + t) Space where s is string 1 and t is string 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}
        for char in s:
            first[char] = first.get(char, 0) + 1
        for char in t:
            second[char] = second.get(char, 0) + 1
        return first == second

# O(s + t) Time | O(s + t) Space, but more optimal on space with only 1 hash
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        first = {}
        for char in s:
            first[char] = first.get(char, 0) + 1
        for char in t:
            first[char] -= 1
            if first[char] < 0:
                return False
        for char in s:
            if first[char] != 0:
                return False
        return True