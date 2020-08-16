# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []

    def peek(self):
        return self.stack[-1][0]

    def pop(self):
        top = self.stack.pop()
        return top[0]

    def push(self, number):
        toPush = [number, number, number]
        if len(self.stack):
            toPush[1] = min(toPush[1], self.stack[-1][1])
            toPush[2] = max(toPush[2], self.stack[-1][2])
        self.stack.append(toPush)

    def getMin(self):
        return self.stack[-1][1]

    def getMax(self):
        return self.stack[-1][2]
