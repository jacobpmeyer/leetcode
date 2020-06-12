def productSum(array, multiplier = 1):
	sum = 0
	for el in array:
		if type(el) is list:
			sum += productSum(el, multiplier + 1)
		else:
			sum += el
	return sum * multiplier