/**
 * @param {number[]} nums
 * @return {number[]}
 */

/**
 * in: array
 * out: int
 *
 * example:
 * 		nums = [1, 2, 3, 4]
 * 		result = [24, 12, 8, 6]
 *
 * steps:
 * 		create an the return array of length nums with 0 at each index
 *
 * 		iterate over the nums array, setting the res array at i as equal to
 * 		nums[i - 1] * res[i - 1]
 *
 * 		create an R variable to represent the running product to the right of i
 *
 * 		iterate over the nums in reverse, starting at len(nums) - 2
 *
 * 		res[i] = res[i - 1] * R
 *
 * 		update R to equal R * num[i - 1]
 *
 * 		return res
 */
var productExceptSelf = function (nums) {
  const res = new Array(nums.length).fill(0);
  res[0] = 1;
  for (let i = 1; i < nums.length; i++) {
    res[i] = res[i - 1] * nums[i - 1];
  }
  let R = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    res[i] = res[i] * R;
    R *= nums[i];
  }
  return res;
};

let nums = [1, 2, 3, 4];
console.log(productExceptSelf(nums)); // => [24, 12, 8, 6]
