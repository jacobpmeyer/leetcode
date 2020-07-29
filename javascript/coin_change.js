/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */

var coinChange = function (coins, amount) {
  const minCoins = new Array(amount + 1).fill(Infinity);
  minCoins[0] = 0;
  coins.forEach(coin => {
    for (i = 1; i < minCoins.length; i++) {
      if (coin <= i) {
        minCoins[i] = Math.min(minCoins[i], minCoins[i - coin] + 1);
      }
    }
  });
  const last = minCoins[minCoins.length - 1];
  return last != Infinity ? last : -1;
};
