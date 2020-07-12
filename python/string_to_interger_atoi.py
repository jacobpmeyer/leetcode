class Solution:
    def myAtoi(self, string: str) -> int:
        maxPos = 2**31
        minPos = -2**31
        nums = "0123456789"
        # left = 0
        # while left < len(string) and string[left] not in nums:
        #     left += 1
        # if left > 0:
        #     if string[left - 1] not in nums and string[left - 1] != "-":
        #         return 0
        # right = left
        # while right < len(string) and string[right] in nums:
        #     right += 1
        string.strip()
        # strInt = int(string[left:right])
        strInt = int(string)
        return strInt
        # if string[left - 1] == "-":
        
        #     strInt = -strInt
        # if strInt > maxPos:
        #     return maxPos
        # if strInt < minPos:
        #     return minPos
        # return strInt