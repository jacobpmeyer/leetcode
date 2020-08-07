// This is the class of the input root.
// Do not edit it.
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

/**
 *
 * @param {BinaryTree} root
 * @return {array}
 *
 * steps:
 * create helper function to handle the recursive nature of the problem
 * Pre-order traverse the Tree, keeping a running branch sum.
 * When a leaf is hit, return the function without altering the sum
 * when a node has neither left or right, push sum to res
 */

function branchSums(root) {
  const arr = [];
  sumHelper(root, 0, arr);
  return arr;
}

function sumHelper(node, sum, sumsArray) {
  if (node === null) return;

  sum += node.value;

  if (!node.left && !node.right) {
    sumsArray.push(sum);
    return;
  }

  sumHelper(node.left, sum, sumsArray);
  sumHelper(node.right, sum, sumsArray);
}

// Do not edit the lines below.
exports.BinaryTree = BinaryTree;
exports.branchSums = branchSums;
