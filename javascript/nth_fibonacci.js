function getNthFib(n, memo = {}) {
  if (n === 1 || n === 2) return n - 1;
  if (memo[n]) return memo[n];
  memo[n] = getNthFib(n - 1) + getNthFib(n - 2);
  return memo[n];
}

// Do not edit the line below.
exports.getNthFib = getNthFib;
