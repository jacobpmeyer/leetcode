class Solution:
    def rob(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        elif len(nums) < 2:
            return nums[0]
        arr = [0 for num in nums]
        arr[0] = nums[0]
        arr[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            arr[i] = max(nums[i] + arr[i - 2], arr[i - 1])
        return arr[-1]