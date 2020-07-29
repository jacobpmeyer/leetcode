def mergeSort(array):
    if len(array) <= 1:
        return array
    auxArray = array[:]
    mergeHelper(array, 0, len(array) - 1, auxArray)
    return array

def mergeHelper(mainArray, startIdx, endIdx, auxArray):
    if startIdx == endIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    mergeHelper(auxArray, startIdx, midIdx, mainArray)
    mergeHelper(auxArray, midIdx + 1, endIdx, mainArray)
    doMerge(mainArray, startIdx, midIdx, endIdx, auxArray)

def doMerge(mainArray, startIdx, midIdx, endIdx, auxArray):
    k = startIdx
    i = startIdx
    j = midIdx + 1
    while i <= midIdx and j <= endIdx:
        if auxArray[i] <= auxArray[j]:
            mainArray[k] = auxArray[i]
            i += 1
        else:
            mainArray[k] = auxArray[j]
            j += 1
        k += 1
    while i <= midIdx:
        mainArray[k] = auxArray[i]
        k += 1
        i += 1
    while j <= endIdx:
        mainArray[k] = auxArray[j]
        k += 1
        j += 1