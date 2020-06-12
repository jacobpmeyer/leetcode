def productSum(array, depth = 1):
	sum = 0
	for el in array:
		if type(el) is List:
			sum += productSum(el, depth + 1):
		else:
			sum += el
	return sum