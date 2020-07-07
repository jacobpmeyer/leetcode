class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums
        first = 0
        second = 1
        while second < len(nums):
            if nums[second] != nums[first]:
                nums[first + 1] = nums[second]
                first += 1
            second += 1
        return nums[:first + 1]