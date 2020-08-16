def balancedBrackets(string):
    bracketStack = []
    opening = { "(", "{", "[" }
    closing = { ")": "(", "}": "{", "]": "[" }
    for char in string:
        if char in opening:
            bracketStack.append(char)
        elif char in closing:
            if len(bracketStack):
                popped = bracketStack.pop()
                if popped != closing[char]:
                    return False
            else:
                return False
    return len(bracketStack) == 0