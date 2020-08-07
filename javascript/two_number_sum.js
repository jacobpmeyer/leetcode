function twoNumberSum(array, targetSum) {
  const h = new Set();
  for (let i = 0; i < array.length; i++) {
    const dif = array[i] - targetSum;
    if (h.has(dif)) {
      return [dif, array[i]];
    }
  }
  return null;
}

const arr = [1, 2, 3, 2];
const targ = 4;
console.log(twoNumberSum(arr, targ));

// Do not edit the line below.
exports.twoNumberSum = twoNumberSum;
