class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        while i < len(nums) and j < len(nums):
            if nums[i] == 0:
                while nums[j] == 0 or i == j:
                    j += 1
                    if j >= len(nums):
                        return nums
                nums[i], nums[j] = nums[j], nums[i]
            i += 1