
# O(n) Time | O(n) Space where n is the length of the input string
# My solution
def balancedBrackets(string):
	lastSeen = []
	for char in string:
		if char == "}":
			if len(lastSeen) and lastSeen[-1] == "{":
				lastSeen.pop()
			else:
				return False
		elif char == ")":
			if len(lastSeen) and lastSeen[-1] == "(":
				lastSeen.pop()
			else:
				return False
		elif char == "]":
			if len(lastSeen) and lastSeen[-1] == "[":
				lastSeen.pop()
			else:
				return False
		elif char == "(" or char == "[" or char == "{":
			lastSeen.append(char)
	return len(lastSeen) == 0

# ae solution
def balancedBrackets(string):
	openingBrackets = "([{"
	closingBrackets = "})]"
	matchingBrackets = { "}": "{", ")": "(", "]": "[" }
	stack = []
	for char in string:
		if char in openingBrackets:
			stack.append(char)
		elif char in closingBrackets:
			if len(stack) == 0:
				return False
			if stack[-1] == matchingBrackets[char]:
				stack.pop()
			else:
				return False
	return len(stack) == 0