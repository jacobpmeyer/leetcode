class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sumsList = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                potentialMatch = [nums[i], nums[left], nums[right]]
                potentialSum = nums[i] + nums[left] + nums[right]
                if potentialSum < 0:
                    left += 1
                elif potentialSum > 0:
                    right -= 1
                else:
                    if not len(sumsList) or sumsList[-1] != potentialMatch:
                        sumsList.append(potentialMatch)
                    left += 1
                    right -= 1
        return sumsList