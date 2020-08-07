/**
 *
 * @param {array} array
 * @param {array} sequence
 * @return {boolean}
 *
 * example:
 * 		array = [1, 2]
 * 		suquence = [1]
 * 		output => true
 *
 * Note:
 * 		the two arrays will never be empty
 *
 * steps:
 * 		2 pointers
 * 		iterate over array
 * 		as going through array, if the current array idx === current sequnce idx:
 * 				iterate the sequence pointer
 *
 * 		if the last of the sequence is present: return true
 * 		if we finish iterating over the array first: return false
 *
 * pseudo:
 * 		let a = 0;
 * 		for i in (0 - array.length) {
 * 			if i == s[a] return true;
 * 		};
 * 		return false;
 */

function isValidSubsequence(array, sequence) {
  let j = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] === sequence[j]) j++;
    if (j === sequence.length) return true;
  }
  return false;
}

let a = [1, 2];
let b = [1, 2];
console.log(isValidSubsequence(a, b));
// Do not edit the line below.
exports.isValidSubsequence = isValidSubsequence;
