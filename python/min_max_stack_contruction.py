# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def __init__(self):
		self.minMaxStack = []
		self.stack = []

	def peek(self):
		return self.stack[-1]

	def pop(self):
		self.minMaxStack.pop()
		return self.stack.pop()

	def push(self, number):
		newMinMax = { "max": number, "min": number }
		if len(self.minMaxStack):
			lastMinMax = self.minMaxStack[-1]
			newMinMax["max"] = max(newMinMax["max"], lastMinMax["max"])
			newMinMax["min"] = min(newMinMax["min"], lastMinMax["min"])
		self.minMaxStack.append(newMinMax)
		self.stack.append(number)

	def getMin(self):
		return self.minMaxStack[-1]["min"]

	def getMax(self):
		return self.minMaxStack[-1]["max"]