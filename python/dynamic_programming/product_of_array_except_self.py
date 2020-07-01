
# Given an array nums of n integers where n > 1,  return an array output such that 
# output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or 
# suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not 
# count as extra space for the purpose of space complexity analysis.)

# O(n) Time | O(n) Space where n is the length of the list
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    length = len(nums)
    left, right, output = [0] * length, [0] * length, [0] * length
    left[0] = 1
    right[-1] = 1
    for i in range(1, length):
      left[i] = left[i - 1] * nums[i - 1]
    for i in reversed(range(length - 1)):
      right[i] = right[i + 1] * nums[i + 1]
    for i in range(length):
      output[i] = left[i] * right[i]
    return output


class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    length = len(nums)
    answer = [0]*length
    answer[0] = 1
    for i in range(1, length):
      answer[i] = nums[i - 1] * answer[i - 1]
    right = 1
    for i in reversed(range(length)):
      answer[i] = answer[i] * right
      right *= nums[i]
    return answer