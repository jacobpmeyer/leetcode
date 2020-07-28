function minHeightBst(array) {
  return bstHelper(array, 0, array.length - 1);
}

function bstHelper(array, startIdx, endIdx) {
  if (startIdx > endIdx) return null;
  const mid = Math.floor((startIdx + endIdx) / 2);
  const root = new BST(array[mid]);
  const right = bstHelper(array, mid + 1, endIdx);
  const left = bstHelper(array, startIdx, mid - 1);
  root.left = left;
  root.right = right;
  return root;
}

class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  insert(value) {
    if (value < this.value) {
      if (this.left === null) {
        this.left = new BST(value);
      } else {
        this.left.insert(value);
      }
    } else {
      if (this.right === null) {
        this.right = new BST(value);
      } else {
        this.right.insert(value);
      }
    }
  }
}

// Do not edit the line below.
exports.minHeightBst = minHeightBst;
