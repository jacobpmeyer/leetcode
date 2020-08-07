function twoNumberSum(array, targetSum) {
  const h = new Set();
  for (let i = 0; i < array.length; i++) {
    const dif = targetSum - array[i];
    if (h.has(dif)) return [dif, array[i]];
    else h.add(array[i]);
  }
  return [];
}

const arr = [1, 2, 2];
const targ = 4;
console.log(twoNumberSum(arr, targ));

// Do not edit the line below.
exports.twoNumberSum = twoNumberSum;
