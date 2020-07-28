function moveElementToEnd(array, toMove) {
  let l = 0;
  let r = array.length - 1;
  while (l < r) {
    while (l < r && array[r] === toMove) r--;
    if (array[l] === toMove) swap(array, l, r);
    l++;
  }
  return array;
}

function swap(arr, l, r) {
  const temp = arr[l];
  arr[l] = arr[r];
  arr[r] = temp;
}

// const array = [2, 1, 2, 2, 2, 3, 4, 2];
// const toMove = 2;

// console.log(moveElementToEnd(array, toMove));

// Do not edit the line below.
exports.moveElementToEnd = moveElementToEnd;
