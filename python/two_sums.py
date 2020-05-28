def twoNumberSum(array, targetSum):
	nums = set()
	for num in array:
		nums.add(num)
	for num in array:
		dif = targetSum - num
		if dif in nums and num != dif:
			return [dif, num]
		
	return []