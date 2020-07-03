def powerset(array):
    powerSet = []
	powerHelper(array, powerSet)
	return powerSet

def powerHelper(array, powerSet):
	if len(array) <= 1:
		powerSet.append(array)
	else:
		for i in range(array):
			powerHelper(array[:i])
			powerHelper(array[i:])
			powerHelper.append(array)