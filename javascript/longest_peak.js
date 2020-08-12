/**
 *
 * @param {array} array
 * @return  {number}
 *
 *
 */

function longestPeak(array) {
  let count = 0;
  let i = 1;
  while (i < array.length) {
    if (array[i] > array[i - 1] && array[i] > array[i + 1]) {
      let tempCount = 1;
      let left = i - 1;
      let right = i + 1;
      while (array[left] < array[left + 1]) {
        tempCount++;
        left--;
      }
      while (array[right] < array[right - 1]) {
        tempCount++;
        right++;
      }
      if (tempCount > count) count = tempCount;
      i = right - 1;
    }
    i++;
  }
  return count;
}

// Do not edit the line below.
exports.longestPeak = longestPeak;
