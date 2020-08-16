def powerset(array):
    sets = [[]]
    for i in range(len(array)):
        for j in range(len(sets)):
            current = sets[j] + [array[i]]
            sets.append(current)
    return sets