function moveElementToEnd(array, toMove) {
  let l = 0;
  let r = array.length - 1;
  while (l < r) {
    while (l < r && array[r] === toMove) {
      r--;
    }
    if (array[l] === toMove) {
      swap(l, r, array);
    }
    l++;
  }
  return array;
}

function swap(i, j, array) {
  const temp = array[i];
  array[i] = array[j];
  array[j] = temp;
}

// Do not edit the line below.
exports.moveElementToEnd = moveElementToEnd;
