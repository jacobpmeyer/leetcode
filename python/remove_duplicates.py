# Given a sorted array nums, remove the duplicates in-place such that each 
# element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying 
# the input array in-place with O(1) extra memory.

class Solution:
	def removeDuplicates(self, array: List[int]) -> int:
		if not len(array):
			return 0
		i = 0
		for j in range(1, len(array)):
			if array[i] != array[j]:
				i += 1
				array[i] = array[j]
		return i + 1