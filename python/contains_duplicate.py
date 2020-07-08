class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsDict = {}
        for num in nums:
            if num in numsDict:
                return True
            else:
                numsDict[num] = True
        return False