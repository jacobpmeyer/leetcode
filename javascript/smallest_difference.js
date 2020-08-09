function smallestDifference(arrayOne, arrayTwo) {
  arrayOne.sort((a, b) => a - b);
  arrayTwo.sort((a, b) => a - b);
  let l = 0;
  let r = 0;
  const smallest = [arrayOne[0], arrayTwo[0]];
  while (l < arrayOne.length && r < arrayTwo.length) {
    const currSmallest = Math.abs(smallest[0] - smallest[1]);
    const maybeSmallest = Math.abs(arrayOne[l] - arrayTwo[r]);
    if (maybeSmallest < currSmallest) {
      smallest[0] = arrayOne[l];
      smallest[1] = arrayTwo[r];
    } else {
      if (arrayOne[l] > arrayTwo[r]) {
        r++;
      } else {
        l++;
      }
    }
  }
  return smallest;
}

// Do not edit the line below.
exports.smallestDifference = smallestDifference;
