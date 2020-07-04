# O(s*n*log(n)) Time | O(sn) Space where s is the length of the words array
# and n is the length of the longest word
def groupAnagrams(words):
	anagrams = {}
	for word in words:
		currentSorted = "".join(sorted(word))
		if currentSorted in anagrams:
			anagrams[currentSorted].append(word)
		else:
			anagrams[currentSorted] = [word]
	return list(anagrams.values())

words = ["yo", "act", "flop", "tac", "cat", "oy", "olfp"]
# [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"]]
print(groupAnagrams(words))