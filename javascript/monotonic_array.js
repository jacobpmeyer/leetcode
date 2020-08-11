// Write a function that takes in an array of integers and returns a boolean
// representing whether the array is monotinic.

// An array is said to be monotonic if its elements, from left to right, are
// entirely non-increasing or entireely non-decreasing.

function isMonotonic(array) {
  let increasing = true;
  let decreasing = true;

  for (let i = 1; i < array.length; i++) {
    if (array[i] > array[i - 1]) {
      increasing = false;
    } else if (array[i] < array[i - 1]) {
      decreasing = false;
    }
  }

  return increasing || decreasing;
}

// Do not edit the line below.
exports.isMonotonic = isMonotonic;
