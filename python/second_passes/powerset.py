def powerset(array):
    sets = [[]]
    for el in array:
        for i in range(len(sets)):
            newSub = sets[i] + [el]
            sets.append(newSub)
    return sets

def powerset(array, idx = None):
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]
    subs = powerset(array, idx - 1)
    for i in range(len(subs)):
        newSub = subs[i] + [array[idx]]
        subs.append(newSub)
    return subs