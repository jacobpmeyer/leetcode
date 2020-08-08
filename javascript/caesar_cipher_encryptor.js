function caesarCipherEncryptor(string, key) {
  const s = [];
  const newKey = key % 26;
  for (const char of string) {
    s.push(charMaker(char, newKey));
  }
  return s.join("");
}

function charMaker(char, key) {
  const newChar = char.charCodeAt() + key;
  return newChar <= 122
    ? String.fromCharCode(newChar)
    : String.fromCharCode(96 + (newChar % 122));
}

// Do not edit the line below.
exports.caesarCipherEncryptor = caesarCipherEncryptor;
