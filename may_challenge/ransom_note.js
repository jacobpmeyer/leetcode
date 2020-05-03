// Given an arbitrary ransom note string and another string containing letters
// from all the magazines, write a function that will return true if the ransom
// note can be constructed from the magazines ; otherwise, it will return false.

// Each letter in the magazine string can only be used once in your ransom note.

// Note:
// You may assume that both strings contain only lowercase letters.

var canConstruct = function (ransomNote, magazine) {
  let count = {};
  for (let i = 0; i < magazine.length; i++) {
    if (count[magazine[i]]) count[magazine[i]]++;
    else count[magazine[i]] = 1;
  }
  for (let i = 0; i < ransomNote.length; i++) {
    if (!count[ransomNote[i]]) return false;
    else count[ransomNote[i]]--;
  }
  return true;
};

console.log(canConstruct("a", "b")); // -> false
console.log(canConstruct("aa", "ab")); // -> false
console.log(canConstruct("aa", "aab")); // -> true
