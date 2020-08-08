function threeNumberSum(array, targetSum) {
  const result = [];
  array.sort((a, b) => a - b);
  for (let i = 0; i < array.length; i++) {
    let l = i + 1;
    let r = array.length - 1;
    while (l < r) {
      const potentialMatch = array[i] + array[l] + array[r];
      if (potentialMatch === targetSum) {
        result.push([array[i], array[l], array[r]]);
        l++;
        r--;
      } else if (potentialMatch < targetSum) {
        l++;
      } else {
        r--;
      }
    }
  }
  return result;
}

// Do not edit the line below.
exports.threeNumberSum = threeNumberSum;
