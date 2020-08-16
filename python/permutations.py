def getPermutations(array):
    perms = []
    permsHelper(0, array, perms)
    return perms

def permsHelper(idx, array, perms):
    if idx == len(array) - 1:
        perms.append(array[:])
    else:
        for j in range(idx, len(array)):
            swap(array, j, idx)
            permsHelper(idx + 1, array, perms)
            swap(array, j, idx)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]