function smallestDifference(arrayOne, arrayTwo) {
  arrayOne.sort((a, b) => a - b);
  arrayTwo.sort((a, b) => a - b);
  console.log(arrayOne, arrayTwo);
  left = 0;
  right = 0;
  smallArr = [arrayOne[0], arrayTwo[0]];
  smallest = Infinity;
  while (left < arrayOne.length && right < arrayTwo.length) {
    console.log(left, right);
    if (Math.abs(arrayOne[left] - arrayTwo[right]) < smallest) {
      smallArr[0] = arrayOne[left];
      smallArr[1] = arrayTwo[right];
      smallest = Math.abs(arrayOne[left] - arrayTwo[right]);
    }
    if (arrayOne[left] < arrayTwo[right]) {
      left++;
    } else if (arrayOne[left] > arrayTwo[right]) {
      right++;
    } else if (arrayOne[left] === arrayTwo[right]) {
      return [left, right];
    }
  }
  return smallArr;
}

arrayOne = [-1, 5, 10, 20, 28, 3];
arrayTwo = [26, 134, 135, 15, 17];
console.log(smallestDifference(arrayOne, arrayTwo)); // [28, 26]

// Do not edit the line below.
exports.smallestDifference = smallestDifference;
