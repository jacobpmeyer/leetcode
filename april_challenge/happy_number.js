// Write an algorithm to determine if a number n is "happy".

// A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

// Return True if n is a happy number, and False if not.

// Example:

// Input: 19
// Output: true
// Explanation:
// 12 + 92 = 82
// 82 + 22 = 68
// 62 + 82 = 100
// 12 + 02 + 02 = 1

// @param {number} n
// @return {boolean}

var isHappy = function (n) {
  let seen = new Set();

  while (!seen.has(n)) {
    seen.add(n);

    let digits = [];

    while (n >= 10) {
      digits.push((n % 10) * (n % 10));
      n = Math.floor(n / 10);
    }
    digits.push(n * n);
    res = digits.reduce((acc, el) => el + acc);
    if (res === 1) {
      return true;
    } else {
      n = res;
    }
  }
  return false;
};

console.log(isHappy(7));
