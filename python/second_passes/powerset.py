def powerset(array):
    sets = [[]]
    for el in array:
        for i in range(len(sets)):
            newSub = sets[i] + [el]
            sets.append(newSub)
    return sets