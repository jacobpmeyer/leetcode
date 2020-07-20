class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i] + nums[i - 1], nums[i])
            maxSoFar = max(maxSoFar, nums[i])
        return maxSoFar

    # Solution using O(n) space in case the input array should not be changed
    def maxSubArray(self, nums: List[int]) -> int:
        arr = [0 for x in nums]
        arr[0] = nums[0]
        maxSoFar = arr[0]
        for i in range(1, len(nums)):
            arr[i] = max(nums[i] + arr[i - 1], nums[i])
            maxSoFar = max(arr[i], maxSoFar)
        return maxSoFar