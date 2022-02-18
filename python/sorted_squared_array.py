# destructive
def sortedSquaredArray(array):
  for i in array:
    el = array[i]
    array[i] = el * el
  return sort(array)


[-10, -5, 0, 5, 10]
