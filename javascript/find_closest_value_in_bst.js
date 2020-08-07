/**
 *
 * @param {TreeNode} tree
 * @param {number} target
 * @return {number}
 *
 * example:
 * 		tree:
 * 				  10
 * 			  /    \
 * 	 	  5       15
 * 	  /  \     /  \
 * 	 2   5    13   22
 *  /          \
 * 1           14
 * 		target: 12
 * 		output: 13 becsause of the node values in the tree, 13 is the closest
 * 			in whole integer distance from target(12)
 *
 * steps:
 * 		create a closestVal variable to keep track of the closest value to target
 * 		create a node variable to keep track of the current node in the tree.
 * 		iterate over nodes by checking whether the node's value is more or less than
 * 			the target node
 * 		traverse right or left subtree accordingly.
 * 		move the node until a we find a leaf
 * 		return closestVal
 *
 * pseudo:
 * 		closestVal = [null, Infinity]; // [13, 1]
 * 		node = tree;
 * 		while (node != null) { // null
 * 			const newDif = Math.abs(target - node.value); // 1
 * 			if (newDif < closestVal[1]) {
 * 				closestVal[0] = node.value;
 * 				closestVal[1] = newDif
 * 			}
 * 			if (node.value < target) node = node.right; // true
 * 			else if (node.value > target) node = node.left;
 * 			else return node.value
 * 		}
 * 		return closestVal[0]
 */

function findClosestValueInBst(tree, target) {
  let closestVal = [null, Infinity];
  let node = tree;
  while (node != null) {
    const newDif = Math.abs(target - node.value);
    if (newDif < closestVal[1]) {
      closestVal[0] = node.value;
      closestVal[1] = newDif;
    }
    if (node.value < target) node = node.right;
    else if (node.value > target) node = node.left;
    else return node.value;
  }
  return closestVal[0];
}

// Do not edit the line below.
exports.findClosestValueInBst = findClosestValueInBst;
