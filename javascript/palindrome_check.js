function isPalindrome(string) {
  let l = 0;
  let r = string.length - 1;
  while (l < r) {
    if (string[l] !== string[r]) {
      return false;
    }
    l++;
    r--;
  }
  return true;
}

const string = "tacocat";
const string2 = "hello";
console.log(isPalindrome(string));
console.log(isPalindrome(string2));

// Do not edit the line below.
exports.isPalindrome = isPalindrome;
