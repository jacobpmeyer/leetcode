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