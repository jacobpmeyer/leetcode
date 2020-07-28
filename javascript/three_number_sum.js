function threeNumberSum(array, targetSum) {
  const trips = [];
  array.sort((a, b) => a - b);
  for (i = 0; i < array.length - 2; i++) {
    let l = i + 1;
    let r = array.length - 1;
    while (l < r) {
      const match = array[i] + array[l] + array[r];
      if (match === targetSum) {
        trips.push([array[i], array[l], array[r]]);
        l++;
        r--;
      } else if (match < targetSum) {
        l++;
      } else if (match > targetSum) {
        r--;
      }
    }
  }
  return trips;
}

// Do not edit the line below.
exports.threeNumberSum = threeNumberSum;
