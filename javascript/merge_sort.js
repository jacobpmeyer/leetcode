function mergeSort(array) {
  if (array.length <= 1) return array;
  const auxArray = array.slice();
  mergeSortHelper(array, 0, array.length - 1, auxArray);
  return array;
}

function mergeSortHelper(mainArray, startIdx, endIdx, auxArray) {
  if (startIdx === endIdx) return;
  const midIdx = Math.floor((startIdx + endIdx) / 2);
  mergeSortHelper(auxArray, startIdx, midIdx, mainArray);
  mergeSortHelper(auxArray, midIdx + 1, endIdx, mainArray);
  doMerge(mainArray, startIdx, midIdx, endIdx, auxArray);
}

function doMerge(mainArray, startIdx, midIdx, endIdx, auxArray) {
  let k = startIdx;
  let i = startIdx;
  let j = midIdx + 1;
  while (i <= midIdx && j <= endIdx) {
    if (auxArray[i] <= auxArray[j]) {
      mainArray[k++] = auxArray[i++];
    } else {
      mainArray[k++] = auxArray[j++];
    }
  }
  while (i <= midIdx) {
    mainArray[k++] = auxArray[i++];
  }
  while (j <= endIdx) {
    mainArray[k++] = auxArray[j++];
  }
}

// Do not edit the line below.
exports.mergeSort = mergeSort;
