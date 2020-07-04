
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

	# O(n^2) Time | O(n^2) Space where n is the length of the string
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
			self.createSuffixSub(i, string)

	def createSuffixSub(self, i, string):
		node = self.root
		for j in range(i, len(string)):
			if string[j] not in node:
				node[string[j]] = {}
			node = node[string[j]]
		node[self.endSymbol] = True

	# O(n) Time | O(1) space where m is the input string
    def contains(self, string):
		node = self.root
		for letter in string:
			if letter not in node:
				return False
			node = node[letter]
		return self.endSymbol in node
