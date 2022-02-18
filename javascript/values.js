function sortedSquaredArray(array) {
	const sorted = new Array(array.length).fill(0);
	let smallerValueIdx = 0;
	let largerValueIdx = array.length - 1;

	for (let i = array.length - 1; i >= 0; i--) {
		const smol = array[smallerValueIdx]
    const chonk = array[largerValueIdx]
		if (Math.abs(smol) > Math.abs(array[largerValueIdx])) {
			sorted[i] = smol * smol
			smallerValueIdx++
		} else {
			sorted[i] = chonk * chonk
      largerValueIdx--
		}
	}

  return sorted
}
