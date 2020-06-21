
# O(n) Time where n is the length of the array.
# O(1) Space
# Not optimal
class Solution:
	def rotate(self, nums: List[int], k: int) -> None:
		pivot = -(k % len(nums))
        nums[:] = nums[pivot:] + nums[:pivot]
		"""
		Do not return anything, modify nums in-place instead.
		"""