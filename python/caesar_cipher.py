def caesarCipherEncryptor(string, key):
	alpha = "abcdefghijklmnopqrstuvwxyz"
	newStr = ""
	for char in string:
		newIdx = (alpha.index(char) + key) % 26
		newStr += alpha[newIdx]
	return newStr