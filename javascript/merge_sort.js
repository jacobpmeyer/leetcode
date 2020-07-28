function mergeSort(array) {
  copyArray = array.split();
  return mergeHelper(array, 0, array.length - 1);
}

// Do not edit the line below.
exports.mergeSort = mergeSort;
