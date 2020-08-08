/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {number}
 */
var pathSum = function (root, sum) {
  let count = 0;
  let k = sum;
  const h = {};
  function preorder(node, currSum) {
    if (node === null) return;
    currSum += node.val;
    if (currSum === k) count += 1;
    if (!(currSum - k in h)) h[currSum - k] = 0;
    count += h[currSum - sum];
    if (!(currSum in h)) h[currSum] = 1;
    else h[currSum] += 1;
    preorder(node.right, currSum);
    preorder(node.left, currSum);
    h[currSum] -= 1;
  }
  preorder(root, 0);
  return count;
};
