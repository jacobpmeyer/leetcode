/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let sold = -Infinity;
  let held = -Infinity;
  let reset = 0;
  prices.forEach(price => {
    const preSold = sold;
    sold = held + price;
    held = Math.max(held, reset - price);
    reset = Math.max(preSold, reset);
  });
  return Math.max(sold, reset);
};
