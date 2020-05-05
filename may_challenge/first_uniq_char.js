var firstUniqChar = function (s) {
  let o = {};
  for (let i = 0; i < s.length; i++) {
    letter = s[i];
    if (o[letter]) {
      o[letter].push(i);
    } else {
      o[letter] = [i];
    }
  }
  for (let i = 0; i < s.length; i++) {
    letter = s[i];
    if (o[letter].length === 1) return o[letter][0];
  }
  return -1;
};

console.log(firstUniqChar("leetcode"));
// return 0.

console.log(firstUniqChar("loveleetcode"));
// return 2.
