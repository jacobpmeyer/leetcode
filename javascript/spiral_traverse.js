function spiralTraverse(array) {
  let startRow = 0;
  let startCol = 0;
  let endRow = array.length - 1;
  let endCol = array[0].length - 1;
  const output = [];

  while (startRow <= endRow && startCol <= endCol) {
    for (let col = startCol; col <= endCol; col++) {
      output.push(array[startRow][col]);
    }
    for (let row = startRow + 1; row <= endRow; row++) {
      output.push(array[row][endCol]);
    }
    for (let col = endCol - 1; col >= startCol; col--) {
      if (startRow === endRow) break;
      output.push(array[endRow][col]);
    }
    for (let row = endRow - 1; row > startRow; row--) {
      if (startCol === endCol) break;
      output.push(array[row][startCol]);
    }
    console.log("startCol: ", startCol, "endCol: ", endCol);
    startCol++;
    startRow++;
    endRow--;
    endCol--;
  }

  return output;
}

// Do not edit the line below.
exports.spiralTraverse = spiralTraverse;
