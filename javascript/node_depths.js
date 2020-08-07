/**
 *
 * @param {BinaryTree} root
 * @return {number}
 *
 * steps:
 * Create helper function to handle additional inputs
 * Helper function take in the tree root and currentDepth
 * Traverse tree
 * At each new node depth, increment the currentDepth by one
 * If tree is not null aka when a leaf is reached, add depth to sum
 *
 * pseudo:
 * if node is null return 0
 * left = depthHelper(node.left, currDepth + 1)
 * right = depthHelper(node.right, currDepth + 2)
 * return left + right + currDepth
 */

function nodeDepths(root) {
  return depthHelper(root, 0);
}

function depthHelper(node, currDepth) {
  if (node === null) return 0;
  const left = depthHelper(node.left, currDepth + 1);
  const right = depthHelper(node.right, currDepth + 1);
  return left + right + currDepth;
}

// This is the class of the input binary tree.
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Do not edit the line below.
exports.nodeDepths = nodeDepths;
