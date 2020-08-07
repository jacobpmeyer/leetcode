function binarySearch(array, target) {
  startIdx = 0;
  endIdx = array.length - 1;
  while (startIdx <= endIdx) {
    const mid = Math.floor((startIdx + endIdx) / 2);
    if (array[mid] === target) {
      return mid;
    } else if (target > array[mid]) {
      startIdx = mid + 1;
    } else {
      endIdx = mid - 1;
    }
  }
  return -1;
}

// Do not edit the line below.
exports.binarySearch = binarySearch;
