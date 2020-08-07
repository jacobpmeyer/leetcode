// Tip: You can use the Array.isArray function to check whether an item
// is a list or an integer.

/**
 *
 * @param {array} array
 * @return {number}
 *
 * steps:
 * reduce the array.
 * the cb should check to see if the element is array
 * if array, recursively call product sum
 * return reduced
 *
 */

function productSum(array, d = 1) {
  let total = 0;
  array.forEach(el => {
    if (Array.isArray(el)) total += d * productSum(el, d + 1);
    else total += d * el;
  });
  return total;
}

// Do not edit the line below.
exports.productSum = productSum;
