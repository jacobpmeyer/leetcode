class Solution:
    def myAtoi(self, string: str) -> int:
        maxPos = 2**31 - 1
        minPos = -2**31
        nums = "0123456789"
        left = 0
        plusMinus = ("-", "+", " ")
        if string == "":
            return 0
        string = string.strip()
        if len(string) == 2 and string[0] not in nums and string[0] not in plusMinus:
            return 0
        while left < len(string) and string[left] not in nums:
            if left > 0 and string[left - 1] not in nums:
                return 0
            left += 1
        if left > 0 and string[left - 1] not in nums and string[left - 1] not in plusMinus:
            return 0
        right = left
        while right < len(string) and string[right] in nums:
            right += 1
        if string[left:right] == "":
            return 0
        strInt = int(string[left:right])
        if left > 0 and string[left - 1] == "-":
            strInt = -strInt
        if strInt > maxPos:
            return maxPos
        if strInt < minPos:
            return minPos
        return strInt