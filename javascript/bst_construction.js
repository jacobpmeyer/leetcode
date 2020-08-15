// Do not edit the class below except for
// the insert, contains, and remove methods.
// Feel free to add new properties and methods
// to the class.
class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  insert(value) {
    if (value >= this.value) {
      if (this.right !== null) this.right.insert(value);
      else this.right = new BST(value);
    } else {
      if (this.left !== null) this.left.insert(value);
      else this.left = new BST(value);
    }
    return this;
  }

  contains(value) {
    let node = this;
    while (node !== null) {
      if (node.value === value) return true;
      else if (node.value > value) node = node.left;
      else node = node.right;
    }
    return false;
  }

  remove(value) {
    let nodeToRemove = null;
    let node = this;
    while (node !== null) {
      if (value === node.value) {
        nodeToRemove = node;
        break;
      } else if (value < node.value) {
        node = node.left;
      } else {
        node = node.right;
      }
    }
    if (nodeToRemove === null) return this;
    node = nodeToRemove.right;
    while (node !== null) {
      if (!node.left) break;
      else node = node.left;
    }
    nodeToRemove.value = node.value;
    node = null;
    return this;
  }
}

// Do not edit the line below.
exports.BST = BST;
